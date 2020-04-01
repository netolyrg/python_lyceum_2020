# date = input('Введите дату в формате ДД/ММ/ГГГГ: ')
# first_dat = date
# dat = date.split('/')
# date = ''.join(dat)


def iter_years():
    for year in range(10000):
        for month in range(1, 13):
            for day in range(1, 32):
                raw_date = '{:02}/{:02}/{:04}'.format(day, month, year)

                date = raw_date.replace('/', '')
                if palindrome_checker(date):
                    print(raw_date)
                else:
                    continue


def palindrome_checker(date):
    if date == date[::-1]:
        return True
    else:
        return False


# print('Is', first_dat, 'a palindrome?', palindrome_checker(date))

print('Palindrome years')
iter_years()
