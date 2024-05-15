from datetime import datetime, timedelta

def days_to_exam(day_count):
    current_date = datetime.now()

    exam_date = current_date + timedelta(days=day_count)

    exam_day = exam_date.day
    exam_month = exam_date.month

    return exam_day, exam_month

try:
    days = int(input("Введите количество дней до экзамена: "))
    exam_day, exam_month = days_to_exam(days)
    print(f"Экзамен состоится {exam_day} числа {exam_month} месяца.")
except ValueError:
    print("Ошибка ввода. Введите целое число.")
