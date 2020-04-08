import time


def count_number(number):
    num = 0

    for i in range(number):
        num += i


def sleep_dear():
    for i in range(10):
        time.sleep(0.09)
        print(f'{10-i} seconds...')


if __name__ == '__main__':
    sleep_dear()
