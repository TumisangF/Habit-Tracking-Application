#  This module offers the 'Analytics' class is used to perform analytics on data
class Analytics:
    def __init__(self, habits):
        self.habits = habits

    def get_all_habits(self):
        return self.habits

    def get_habits_by_periodicity(self, periodicity):
        #  Returns a list of habits for the period of day or week.
        return [habit for habit in self.habits if habit.periodicity == periodicity]

    def get_longest_run_streak(self):
        longest_streak = 0
        for habit in self.habits:
            streak = habit.get_run_streak()
            if streak > longest_streak:
                longest_streak = streak
        return longest_streak

    def get_longest_run_streak_for_habit(self, habit_name):
        # Returns a longest streak ran for any given habit
        habit = next((h for h in self.habits if h.name == habit_name), None)
        if habit:
            return habit.get_run_streak()
        return 0
