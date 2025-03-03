class GoalException(Exception):
    def __init__(self, message="Agent could not find the goal state"):
        self.message = message
        super().__init__(self.message)
