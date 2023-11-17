import sqlite3

# Создание базы данных и таблицы
def create_database():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 topic TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Функция для добавления данных в базу
def add_student(name, topic):
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute("INSERT INTO students (name, topic) VALUES (?, ?)", (name, topic))
    conn.commit()
    conn.close()

# Функция для просмотра всех данных
def view_students():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    rows = c.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Topic: {row[2]}")
    conn.close()

# Функция для изменения данных
def update_student(id, name, topic):
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute("UPDATE students SET name=?, topic=? WHERE id=?", (name, topic, id))
    conn.commit()
    conn.close()

# Функция для удаления данных
def delete_student(id):
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()

# Функция для поиска данных по теме
def search_student(topic):
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE topic=?", (topic,))
    rows = c.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Topic: {row[2]}")
    conn.close()

# Создание базы данных при запуске программы
create_database()

# Пример использования функций
add_student("Иван", "Искусственный интеллект")
add_student("Мария", "Биоинформатика")
add_student("Алексей", "Кибербезопасность")

print("Все студенты:")
view_students()

print("\nПоиск студентов по теме 'Искусственный интеллект':")
search_student("Искусственный интеллект")

print("\nОбновление данных студента с ID=1:")
update_student(1, "Николай", "Машинное обучение")

print("\nУдаление студента с ID=2:")
delete_student(2)

print("\nОбновленный список студентов:")
view_students()
