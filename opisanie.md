# Отчёт по лабораторной работе №2

## 1. Создание базы данных

Для выполнения лабораторной работы была создана база данных **study** в системе **PostgreSQL**.
Создание базы данных выполнялось в среде **pgAdmin 4** при помощи следующего SQL-запроса:

```sql
CREATE DATABASE study
    WITH
    OWNER = mihaililicev
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.UTF-8'
    LC_CTYPE = 'en_US.UTF-8'
    ICU_LOCALE = 'en-US'
    LOCALE_PROVIDER = 'icu'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
```

Данная команда создаёт базу данных с владельцем *mihaililicev* и кодировкой **UTF-8**, обеспечивающей корректную работу с текстовыми данными.
После выполнения запроса база данных появилась в списке подключений PostgreSQL и использовалась для дальнейшего создания таблиц.

## 2. Создание таблицы `students`

Таблица **students** предназначена для хранения данных о студентах: их идентификатора, имени и номера курса.
Создание таблицы выполнялось с помощью следующего SQL-запроса:

```sql
CREATE TABLE IF NOT EXISTS public.students
(
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    student_name VARCHAR(64) NOT NULL,
    course_number INT NOT NULL CHECK (course_number >= 1 AND course_number <= 8)
);
```

**Описание структуры таблицы:**

* `id` — уникальный идентификатор студента, создаётся автоматически и является первичным ключом;
* `student_name` — имя студента, обязательное для заполнения;
* `course_number` — номер курса, принимает значения от 1 до 8 (проверяется ограничением `CHECK`).

**Ограничения целостности:**

* `PRIMARY KEY (id)` — уникальность записи;
* `CHECK (course_number >= 1 AND course_number <= 8)` — контроль допустимых значений курса.

После создания таблицы в неё были загружены данные из CSV-файла, содержащего список студентов и их курсы.

## 3. Создание таблицы `disciplines`

Таблица **disciplines** используется для хранения информации о расписании занятий по дисциплинам для разных курсов.
Создание таблицы выполнялось с помощью следующего SQL-запроса:

```sql
CREATE TABLE disciplines (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    discipline_name VARCHAR(255) NOT NULL,
    day_of_week VARCHAR(20) NOT NULL CHECK (day_of_week IN ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')),
    pair_number INT NOT NULL CHECK (pair_number >= 1 AND pair_number <= 8),
    course_number INT NOT NULL CHECK (course_number >= 1 AND course_number <= 8),
    CONSTRAINT unique_schedule UNIQUE (day_of_week, pair_number, course_number)
);
```

**Описание структуры таблицы:**

* `id` — уникальный идентификатор дисциплины;
* `discipline_name` — название дисциплины;
* `day_of_week` — день недели проведения занятия (допустимы только значения от Monday до Sunday);
* `pair_number` — номер пары (от 1 до 8);
* `course_number` — номер курса, для которого проводится занятие;
* `unique_schedule` — ограничение, предотвращающее дублирование занятий по одному курсу на один и тот же день и пару.

**Ограничения целостности:**

* Первичный ключ (`PRIMARY KEY (id)`) обеспечивает уникальность каждой дисциплины;
* Проверочные ограничения (`CHECK`) контролируют корректность данных;
* Уникальное ограничение (`UNIQUE`) предотвращает пересечение расписания.



