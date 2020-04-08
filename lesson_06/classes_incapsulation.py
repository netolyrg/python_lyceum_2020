class User:
    def __init__(self, name):
        self.__name = name


if __name__ == '__main__':
    user = User('Yan')

    print(user._User__name)

