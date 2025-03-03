from search.nim import Nim
from search.nim.nim_agent import NimAgent
from search.nim.nim_result_estimation_functions import no_winner_function


class MinimaxNimAgent(NimAgent):
    def __init__(self, nim_start: Nim = None, limit: int = 10):
        super().__init__(nim_start)
        self._explored_options = {}
        self.limit = limit

    def search_agent(self, show_visuals: bool = True, heuristic_function=None, opponent_starts=False):
        start_nim = self._nim_start_state
        option = self.minimax(start_nim, True, self.limit, heuristic_function)
        return option[1], option[2]

    def minimax(self, nim: Nim, max_value: bool, limit: int, estimating_function):
        possible_moves = self._check_possible_moves(nim)
        values = []
        for new_nim, tower, count in possible_moves:
            if new_nim == self._nim_goal_state:
                return (1, tower, count) if max_value else (-1, tower, count)
            if new_nim in self._explored_options and max_value in self._explored_options[new_nim]:
                return self._explored_options[new_nim][max_value], tower, count
            elif limit == 1:
                return (estimating_function(new_nim), tower,
                        count) if estimating_function is not None else (no_winner_function(), tower, count)
            else:
                value, tower, count = self.minimax(new_nim, not max_value, limit - 1, estimating_function)
            if (max_value and value == 1) or (not max_value and value == -1):
                if new_nim not in self._explored_options:
                    self._explored_options[new_nim] = {}
                self._explored_options[new_nim][max_value] = value
                return value, tower, count
            values.append((value, tower, count))
        return_group = (values[0][0], values[0][1], values[0][2]) # noqa
        for value, tower, count in values[1:]:
            if (max_value and value > return_group[0]) or (not max_value and value < return_group[0]):
                return_group = (value, tower, count)
        return return_group

    def __str__(self):
        return "Minimax Agent"
