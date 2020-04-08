#  Простой класс с атрибутами


class User:
    def __init__(self, name):
        self.name = name
        print('Created!')

    def say_hello(self):
        print(f'Hello! My name is {self.name}')


if __name__ == '__main__':
    # create an object of User
    first_user = User('Alex')
    first_user.say_hello()

    second_user = User('Alice')
    second_user.say_hello()
