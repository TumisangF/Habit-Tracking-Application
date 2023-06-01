import datetime

"""
The 'Habit' class provided in ths module is used to describe a habit and track its progress.
"""

class Habit:
    def __init__(self, name, periodicity):
        self.name = name
        self.periodicity = periodicity
        self.creation_date = datetime.datetime.now()
        self.completed_tasks = []

    def add_completed_task(self):
        # Adds an activity accomplished to the habit
        self.completed_tasks.append(datetime.datetime.now())

    def get_run_streak(self):
        # calculates the habit's current run streak and returns it.
        streak = 0
        today = datetime.date.today()
        for task in reversed(self.completed_tasks):
            if task.date() == today:
                streak += 1
                today -= datetime.timedelta(days=1)
            else:
                break
        return streak
