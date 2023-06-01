#This module uses a `HabitDatabase` class to store data in a SQlite3 database.
import datetime
import sqlite3
from habit import Habit

class HabitDatabase:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS habits
                     (name TEXT, periodicity TEXT, creation_date TEXT, completed_tasks TEXT)''')
        self.conn.commit()

    def add_habit(self, habit):
        c = self.conn.cursor()
        c.execute("INSERT INTO habits VALUES (?, ?, ?, ?)",
                  (habit.name, habit.periodicity, habit.creation_date, str(habit.completed_tasks)))
        self.conn.commit()

    def get_habits(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM habits")
        rows = c.fetchall()
        habits = []
        for row in rows:
            habit = Habit(row[0], row[1])
            habit.creation_date = datetime.datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S.%f')
            habit.completed_tasks = eval(row[3])
            habits.append(habit)
        return habits

    def update_habit(self, habit):
        c = self.conn.cursor()
        c.execute("UPDATE habits SET completed_tasks=? WHERE name=?", (str(habit.completed_tasks), habit.name))
        self.conn.commit()
