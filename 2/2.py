import sqlite3
from fastapi import FastAPI

app = FastAPI()

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
    students = []
    for row in rows:
        students.append({"id": row[0], "name": row[1], "topic": row[2]})
    conn.close()
    return students

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
    students = []
    for row in rows:
        students.append({"id": row[0], "name": row[1], "topic": row[2]})
    conn.close()
    return students

# Создание базы данных при запуске программы
create_database()

# API Endpoints

@app.post("/students/")
def create_student(name: str, topic: str):
    add_student(name, topic)
    return {"message": "Student created successfully"}

@app.get("/students/")
def get_students():
    students = view_students()
    return {"students": students}

@app.put("/students/{student_id}")
def update_student(student_id: int, name: str, topic: str):
    update_student(student_id, name, topic)
    return {"message": "Student updated successfully"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    delete_student(student_id)
    return {"message": "Student deleted successfully"}

@app.get("/students/search/")
def search_students(topic: str):
    students = search_student(topic)
    return {"students": students}
