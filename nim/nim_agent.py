import copy
from abc import ABC, abstractmethod
import random
import numpy as np
from nim import Nim


class NimAgent(ABC):
    _frontier: list = []
    _explored_states: list = []
    _steps_count: int = 0

    def __init__(self, nim_start: Nim = None):
        if nim_start is not None:
            self._nim_start_state = copy.deepcopy(nim_start)
            towers = np.zeros(len(nim_start.towers)).tolist()
            self._nim_goal_state = Nim(towers=towers)

    def reset_agent(self, nim_start: Nim = None):
        if nim_start is not None:
            self._nim_start_state = copy.deepcopy(nim_start)
            towers = np.zeros(len(nim_start.towers)).tolist()
            self._nim_goal_state = Nim(towers=towers)
        self._frontier.clear()
        self._explored_states.clear()
        self._steps_count = 0

    @abstractmethod
    def search_agent(self, show_visuals: bool = True, heuristic_function=None, opponent_starts=False):
        pass

    def _check_possible_moves(self, nim: Nim) -> list:
        possible_moves = nim.get_possible_moves()
        possible_nims = []
        for move in possible_moves:
            new_nim = copy.deepcopy(nim)
            new_nim.move(move[0], move[1])
            possible_nims.append((new_nim, move[0], move[1]))
        return possible_nims

    @staticmethod
    def _sim_opponent_move_random(nim: Nim) -> (Nim, int, int):
        possible_moves = nim.get_possible_moves()
        move = random.choice(possible_moves)
        new_nim = copy.deepcopy(nim)
        new_nim.move(move[0], move[1])
        return new_nim, move[0], move[1]

    def _set_state_as_explored(self, nim: Nim):
        self._explored_states.append(nim)


class NimState:
    def __init__(self, nim: Nim, previous_cost: int, estimated_cost: int, moves: list):
        self.nim = nim
        self.previous_cost = previous_cost
        self.estimated_cost = estimated_cost
        self.moves = moves

    def __lt__(self, other):
        return self.estimated_cost < other.estimated_cost

    def __eq__(self, other):
        return self.nim == other.nim

    def visualize_game(self) -> None:
        if len(self.moves) == 0:
            print('No previous moves')
        else:
            for move in self.moves:
                if move[0] == 'P':
                    print('Player ', end='')
                else:
                    print('Opponent ', end='')
                print(f'remove {move[2]} from tower number {move[1]}')
        self.nim.visualize_game()

    def add_player_move(self, tower, count):
        self.moves.append(('P', tower, count))
