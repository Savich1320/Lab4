import random

def generate_schedule(num_exams, disciplines):
    days_of_week = ['понедельник', 'вторник', 'среду', 'четверг', 'пятницу']
    exam_times = [9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0]

    for _ in range(num_exams):
        discipline = random.choice(disciplines)
        disciplines.remove(discipline)

        day = random.choice(days_of_week)
        time = random.choice(exam_times)
        exam_times.remove(time)

        ticket_number = random.randint(1, 20)

        print(f"Экзамен по дисциплине «{discipline}» состоится в {day} время {time}. Ваш счастливый билет N {ticket_number}.")

num_exams = int(input("Введите количество экзаменов: "))
disciplines = input("Введите названия дисциплин через запятую и пробел: ").split(", ")

generate_schedule(num_exams, disciplines)
