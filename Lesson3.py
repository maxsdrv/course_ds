

def lesson3():
    cor_dict = {0.3: 'weak', -0.3: 'weak', 0.96: 'strong'}
    lst = []
    val_to_find = 'weak'

    for key, value in cor_dict.items():
        if value == val_to_find:
            lst.append(key)

    print(*lst, sep=" ")

    numbers = [1, 2, 3, 4, 5]
    for number in numbers:
        print(number * 2)

    [print(number * 2) for number in numbers]


class Users:
    def __init__(self, data):
        print(f"Data= ", *data, sep=",")
        self.data = data

    def check_user(self, user, pwd):
        ex = self.data[user] == pwd if user in self.data else False

        # if user in self.data:
        #     ex = self.data[user] == pwd
        # else:
        #     ex = False

        return ex


if __name__ == '__main__':
    users = Users({"user": "password",
                   "iseedeadpeope": "greedisgood",
                   "hesoyam": "tgm"})

    print(users.check_user("user", "password"))
