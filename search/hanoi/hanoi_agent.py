import bisect
import copy
from abc import ABC, abstractmethod
from search.hanoi import Hanoi


class HanoiAgent(ABC):
    _hanoi_start_state: Hanoi
    _hanoi_goal_state: Hanoi
    _frontier: list = []
    _explored_states: list = []
    _steps_count: int = 0

    def __init__(self, hanoi_start: Hanoi = None, hanoi_goal: Hanoi = None):
        self._hanoi_start_state = copy.deepcopy(hanoi_start)
        self._hanoi_goal_state = copy.deepcopy(hanoi_goal)

    def reset_agent(self, hanoi_start: Hanoi, hanoi_goal: Hanoi):
        self._hanoi_start_state = copy.deepcopy(hanoi_start)
        self._hanoi_goal_state = copy.deepcopy(hanoi_goal)
        self._frontier.clear()
        self._explored_states.clear()
        self._steps_count = 0

    @abstractmethod
    def search_agent(self, show_visuals: bool = True, heuristic_function=None):
        pass

    def _check_possible_moves(self, hanoi: Hanoi, cost: int = 0, heuristic_function=None) -> int:
        possible_moves = hanoi.get_possible_moves()
        possible_moves_count = 0
        for move in possible_moves:
            new_hanoi = copy.deepcopy(hanoi)
            new_hanoi.move(move[0], move[1])
            if new_hanoi not in self._explored_states and HanoiState(new_hanoi, 0, 0) not in self._frontier:
                if heuristic_function:
                    bisect.insort(self._frontier, HanoiState(new_hanoi, cost + 1, heuristic_function(hanoi) + cost + 1))
                else:
                    self._frontier.append(HanoiState(new_hanoi, cost + 1, 0))
                possible_moves_count += 1
        return possible_moves_count

    def _set_state_as_explored(self, hanoi: Hanoi):
        self._explored_states.append(hanoi)


class HanoiState:
    def __init__(self, hanoi: Hanoi, previous_cost: int, estimated_cost: int):
        self.hanoi = hanoi
        self.previous_cost = previous_cost
        self.estimated_cost = estimated_cost

    def __lt__(self, other):
        return self.estimated_cost < other.estimated_cost

    def __eq__(self, other):
        return self.hanoi == other.hanoi
