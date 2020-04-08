#  Простой класс со свойствами


class User:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender
        print('Created!')

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def gender(self):
        return self.__gender

    @name.setter
    def name(self, new_name):
        if new_name != '':
            self.__name = new_name
        else:
            self.__name = self.__name
            print('Wrong name!')

    def say_hello(self):
        print(f'Hello! My name is {self.name}, I\'m {self.age} years old!')
        self.__increase_age()

    def __increase_age(self):
        self.__age += 1


if __name__ == '__main__':
    # create an object of User
    first_user = User('Alex', 22, 'male')
    first_user.say_hello()
    first_user.say_hello()
    first_user.say_hello()
