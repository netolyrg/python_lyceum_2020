# import datetime
from datetime import datetime, timedelta


def day_of_birth(date):
    week_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    date = datetime.strptime(date, '%d %m %Y')
    return week_days[date.weekday()]


if __name__ == '__main__':
    today = datetime.today()

    days = int(input())
    print(today - timedelta(days=days))  # seconds minutes hours days weeks years
