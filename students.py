import psycopg2
from psycopg2.extras import DictCursor


# Функция подключения к базе данных PostgreSQL
def connect():
    study = {
        'dbname':'study',       
        'user': 'postgres',        
        'password': 'postgres',    
        'host': 'localhost',       
        'port': '5432'             
    }
    return psycopg2.connect(**study)  # возвращаем объект подключения


# Получение одного студента по ID
def get_student(id_student):
    with connect() as conn:  
        with conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute('SELECT student_name FROM students WHERE id = %s', (id_student,))
            return cur.fetchone()  


# Получение дисциплин по номеру курса
def get_discipline(number_course):
    with connect() as conn:
        with conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(
                '''
                SELECT discipline_name
                FROM disciplines
                WHERE course_number = %s
                ORDER BY day_of_week, pair_number
                ''',
                (number_course,)
            )
            return cur.fetchall()


# Получение всех студентов по номеру курса
def get_students(course_number):
    with connect() as conn:
        with conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(
                'SELECT student_name FROM students WHERE course_number = %s ORDER BY student_name',
                (course_number,)
            )
            return cur.fetchall()


# Получение полного расписания (все дисциплины)
def get_disciplines():
    with connect() as conn:
        with conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(
                'SELECT id, discipline_name, day_of_week, pair_number, course_number FROM disciplines'
            )
            return cur.fetchall()


# Добавление нового студента
def put_student(student_name, course_number):
    with connect() as conn:
        with conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(
                '''
                INSERT INTO students (student_name, course_number)
                VALUES (%s, %s)
                RETURNING id
                ''',
                (student_name, course_number)
            )
            id_students = cur.fetchone()['id']  # получаем ID нового студента
            conn.commit()  # сохраняем изменения
            return id_students


# Добавление новой дисциплины в расписание
def put_discipline(discipline_name, day_of_week, pair_number, course_number):
    with connect() as conn:
        with conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(
                '''
                INSERT INTO disciplines (discipline_name, day_of_week, pair_number, course_number)
                VALUES (%s, %s, %s, %s)
                RETURNING id
                ''',
                (discipline_name, day_of_week, pair_number, course_number)
            )
            id_discipline = cur.fetchone()['id']
            conn.commit()
            return id_discipline


# Удаление студента по ID
def delete_student(id_student):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute('DELETE FROM students WHERE id = %s', (id_student,))
            conn.commit()


# Удаление дисциплины по ID
def delete_discipline(id_discipline):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute('DELETE FROM disciplines WHERE id = %s', (id_discipline,))
            conn.commit()