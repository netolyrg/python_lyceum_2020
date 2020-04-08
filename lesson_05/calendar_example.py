# import datetime
from datetime import datetime
import calendar


def day_of_birth(date):
    # week_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    date = datetime.strptime(date, '%d %m %Y')
    return calendar.day_name[date.weekday()]


if __name__ == '__main__':
    c = calendar.LocaleTextCalendar(locale="ru_RU.UTF-8")
    c.prmonth(themonth=1, theyear=2024)
