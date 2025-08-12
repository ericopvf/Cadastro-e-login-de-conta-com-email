import datetime

class database:
    def __init__(self, filename):
        self.filename = filename
        self.users = {}
        self.load()

    def load(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    email, password, name, created = line.strip().split(";")
                    self.users[email] = (password, name, created)
        except FileNotFoundError:
            open(self.filename, "w").close()

    def get_user(self, email):
        return self.users.get(email, -1)

    def add_user(self, email, password, name):
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip(), database.get_date())
            self.save()
            return 1
        else:
            print("Email exists already")
            return -1

    def validate(self, email, password):
        return self.get_user(email) != -1 and self.users[email][0] == password

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]
