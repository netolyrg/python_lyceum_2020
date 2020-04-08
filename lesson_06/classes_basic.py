#  Простой класс


class User:
    def __init__(self):
        print('Created!')

    def say(self):
        print('Hello!')


if __name__ == '__main__':
    # create an object of User
    user = User()
    user.say()  # will print "Hello!"

