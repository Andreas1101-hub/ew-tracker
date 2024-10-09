import sqlite3
from flask import Flask, request, redirect
from datetime import datetime

class Database:
    def __init__(self, url="database.db"):
        with sqlite3.connect(url) as db:
            cursor = db.cursor()
            sql = """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_name TEXT NOT NULL,
                subject TEXT NOT NULL,
                beak TEXT NOT NULL,
                due_date DATE NOT NULL
            );
            """
            cursor.execute(sql)

            sql_insert = """
            INSERT INTO tasks (task_name, subject, beak, due_date) VALUES (?, ?, ?, ?);
            """
            
            tasks = [
                ('Task1', 'Subject1', 'Beak1', '2024-11-01'),
                ('Task2', 'Subject2', 'Beak2', '2024-11-01'),
                ('Task3', 'Subject3', 'Beak3', '2024-11-01'),
                ('Task4', 'Subject4', 'Beak4', '2024-11-01'),
                ('Task5', 'Subject5', 'Beak5', '2024-11-01'),
                ('Task6', 'Subject6', 'Beak6', '2024-11-01'),
                ('Task7', 'Subject7', 'Beak7', '2024-11-01'),
                ('Task8', 'Subject8', 'Beak8', '2024-11-01'),
                ('Task9', 'Subject9', 'Beak9', '2024-11-01'),
                ('Task10', 'Subject10', 'Beak10', '2024-11-01')
            ]

            cursor.executemany(sql_insert, tasks)
            db.commit()

    def get_ews(self):
        with sqlite3.connect("database.db") as db:
            cursor = db.cursor()
            sql = """ 
            SELECT id, task_name, subject, beak, due_date FROM tasks
            """
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
    
    def create_ew():
        task = request.form['Task']
        subject = request.form['Subject']
        beak = request.form['Beak']
        due_date = request.form['Due Date']
        with sqlite3.connect("database.db") as db:
            cursor = db.cursor()
            sql_insert = """
            INSERT INTO tasks (task_name, subject, beak, due_date) 
            VALUES (?, ?, ?, ?);
            """
            cursor.execute(sql_insert, (task, subject, beak, due_date))
            db.commit()

    # EXTRA CREDIT
    def get_ew(self, id):
        """
        TO IMPLEMENT
        """
        pass