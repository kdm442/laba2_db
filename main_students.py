from colorama import init, Fore, Back, Style
init(autoreset=True)

from students import (
    get_student,
    get_discipline,
    get_students,
    get_disciplines,
    put_student,
    put_discipline,
    delete_student,
    delete_discipline
)

def main():
    print(Fore.GREEN + "\n-------------API для базы данных study----------------")
    print("get student <id> - получить студента по ID")
    print("get discipline <course_number> - получить дисциплины по номеру курса")
    print("get students <course_number> - получить всех студентов по курсу")
    print("get disciplines - получить полное расписание дисциплин")
    print("put student <student_name> <course_number> - добавить нового студента")
    print("put discipline <discipline_name> <day_of_week> <pair_number> <course_number> - добавить дисциплину")
    print("delete student <id> - удалить студента по ID")
    print("delete discipline <id> - удалить дисциплину по ID")
    print("exit - выход из программы\n")
    print("Введите команду или 'exit' для выхода.\n")

    while True:
        inp = input(" ").strip().split()
        if not inp:
            continue
        if inp[0].lower() == 'exit':
            print("Выход из программы.")
            break

        command = inp[0].lower()

        if command == 'get':
            if inp[1] == 'student':
                student = get_student(int(inp[2]))
                if student:
                    print(*student)
                else:
                    print(Fore.RED +"Студент не найден")

            elif inp[1] == 'discipline':
                disciplines = get_discipline(int(inp[2]))
                if disciplines:
                    for d in disciplines:
                        print(*d)
                else:
                    print(Fore.RED +"Нет дисциплин для указанного курса")

            elif inp[1] == 'students':
                students = get_students(int(inp[2]))
                if students:
                    for s in students:
                        print(*s)
                else:
                    print(Fore.RED +"Нет студентов на указанном курсе")

            elif inp[1] == 'disciplines':
                disciplines = get_disciplines()
                for ds in disciplines:
                    print(*ds)

        elif command == 'put':
            if inp[1] == 'student':
                try:
                    course_number = int(inp[-1])
                    student_name = " ".join(inp[2:-1])
                    new_id = put_student(student_name, course_number)
                    print(f"Студент '{student_name}' добавлен с id {new_id}")
                except Exception as e:
                    print(Fore.RED + f"Ошибка при добавлении студента: {e}")

            elif inp[1] == 'discipline':
                try:
                    discipline_name = " ".join(inp[2:-3])
                    day_of_week = inp[-3]
                    pair_number = int(inp[-2])
                    course_number = int(inp[-1])
                    new_id = put_discipline(discipline_name, day_of_week, pair_number, course_number)
                    print(f"Дисциплина '{discipline_name}' добавлена с id {new_id}")
                except Exception as e:
                    print(Fore.RED + f"Ошибка при добавлении дисциплины: {e}")

        elif command == 'delete':
            if inp[1] == 'student':
                try:
                    delete_student(int(inp[2]))
                    print("Студент удалён.")
                except Exception as e:
                    print(Fore.RED + f"Ошибка при удалении студента: {e}")

            elif inp[1] == 'discipline':
                try:
                    delete_discipline(int(inp[2]))
                    print("Дисциплина удалена.")
                except Exception as e:
                    print(Fore.RED + f"Ошибка при удалении дисциплины: {e}")
        else:
            print(Fore.RED + "Неизвестная команда. Введите 'exit' для выхода.")


if __name__ == "__main__":
    main()
