class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

user1 = User("Maider", "Igorre")
print(user1.username, user1.password)
