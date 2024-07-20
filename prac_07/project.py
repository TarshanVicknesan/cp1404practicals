class Project:
    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percent_complete = percent_complete

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, " \
               f"priority: {self.priority}, cost estimate: {self.cost_estimate:.2f}, " \
               f"completion: {self.percent_complete}%"

    def __lt__(self, other):
        return self.priority < other.priority

    def update_details(self, priority=None, cost_estimate=None, percent_complete=None):
        """
        Update the project's priority, cost estimate, or completion percentage.
        """
        if priority is not None:
            self.priority = priority
        if cost_estimate is not None:
            self.cost_estimate = cost_estimate
        if percent_complete is not None:
            self.percent_complete = percent_complete

    def is_complete(self):
        """
        Check if the project is complete (100%).
        """
        return self.percent_complete == 100

    def remaining_cost(self):
        """
        Calculate the remaining cost based on the completion percentage.
        """
        return self.cost_estimate * (1 - self.percent_complete / 100.0)
