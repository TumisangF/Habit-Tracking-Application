import datetime
import sys
from habit import Habit
from analytics import Analytics
from database import HabitDatabase

def print_habits(habits):
    print("Current Habits:")
    for habit in habits:
        print(f"- {habit.name} ({habit.periodicity})")
    print()

def add_habit(habit_name, periodicity, habits, db):
    habit = Habit(habit_name, periodicity)
    habits.append(habit)
    db.add_habit(habit)
    print(f"Habit '{habit.name}' added!\n")

def check_off_habit(habit_name, habits, db):
    habit = next((h for h in habits if h.name == habit_name), None)
    if habit:
        habit.add_completed_task()
        db.update_habit(habit)
        print(f"Habit '{habit.name}' checked off!\n")
    else:
        print(f"Habit '{habit_name}' not found!\n")

def main():
    predefined_habits = [
        ("Drink water", "daily"),
        ("Exercise", "daily"),
        ("Read a book", "daily"),
        ("Take a walk", "weekly"),
        ("Meditate", "daily")
    ]

    habits = []
    db = HabitDatabase("habits.db")
    habits += db.get_habits()
    """"
    To resemble a time frame of 4 weeks in the past for the sample tracking data, 
    28 days (a month/4 weeks) are subtracted from the "creation_date". 
    This allows for tracking data spanning a period of 4 weeks 
    when the habits were already being tracked by changing the creation_date of the specified habits to an earlier date.
    """
    if not habits:
        for name, periodicity in predefined_habits:
            habit = Habit(name, periodicity)
            habit.creation_date -= datetime.timedelta(days=28) 
            for i in range(28):
                if periodicity == "daily":
                    if i % 2 == 0:
                        habit.add_completed_task()
                elif periodicity == "weekly":
                    if i % 7 == 0:
                        habit.add_completed_task()
            habits.append(habit)
            db.add_habit(habit)

    analytics = Analytics(habits)

    while True:
        print("")
        print("*****************************************\nWelcome to the Habit Tracking Application\n*****************************************")
        print("1. Print all habits")
        print("2. Add a habit")
        print("3. Check off a habit")
        print("4. Print habits by periodicity")
        print("5. Print longest run streak")
        print("6. Print longest run streak for a habit")
        print("7. Exit Application")

        choice = input("\nPlease enter your choice (1-7): ")

        if choice == "1":
            print_habits(analytics.get_all_habits())
        elif choice == "2":
            habit_name = input("Enter the habit name: ")
            periodicity = input("Enter the periodicity (daily/weekly): ")
            add_habit(habit_name, periodicity, habits, db)
        elif choice == "3":
            habit_name = input("Enter the habit name: ")
            check_off_habit(habit_name, habits, db) 
        elif choice == "4":
            periodicity = input("Enter the periodicity (daily/weekly): ")
            habits_by_periodicity = analytics.get_habits_by_periodicity(periodicity)
            print_habits(habits_by_periodicity)
        elif choice == "5":
            longest_streak = analytics.get_longest_run_streak()
            print(f"Longest run streak: {longest_streak}\n")
        elif choice == "6":
            habit_name = input("Enter the habit name: ")
            longest_streak = analytics.get_longest_run_streak_for_habit(habit_name)
            print(f"Longest run streak for '{habit_name}': {longest_streak}\n")
        elif choice == "7":
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
