from datetime import datetime, timedelta

def is_lucky_day(date):
    return date.day % 4 != 0 and date.weekday() != 0

def find_lucky_dates(start_date, n, count):
    lucky_dates = []
    current_date = start_date

    while len(lucky_dates) < count:
        if is_lucky_day(current_date):
            lucky_dates.append(current_date.strftime("%d %B, %A"))
        current_date += timedelta(days=n)

    return lucky_dates

try:
    start_date_str = input("Введите исходную дату в формате YYYY/MM/DD: ")
    n = int(input("Введите число n: "))
    count = 3

    start_date = datetime.strptime(start_date_str, "%Y/%m/%d")
    lucky_dates = find_lucky_dates(start_date, n, count)

    print("Счастливые даты экзамена:")
    for date in lucky_dates:
        print(date)
except ValueError:
    print("Ошибка ввода. Проверьте правильность формата даты и введенных данных.")
