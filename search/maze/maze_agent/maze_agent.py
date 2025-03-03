import bisect
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.use('TkAgg')


class MazeAgent(ABC):
    _maze: np.ndarray
    _start_x: int
    _start_y: int
    _goal_x: int
    _goal_y: int
    _frontier: list = []
    _explored_states: list = []
    _maze_type: str
    _steps_count: int = 0

    def __init__(self, maze: np.ndarray = None, maze_type: str = None, start_x: int = 0, start_y: int = 0,
                 goal_x: int = 0, goal_y: int = 0):
        if maze:
            self.change_maze(maze, maze_type, start_x, start_y, goal_x, goal_y)

    def change_maze(self, maze: np.ndarray = None, maze_type: str = None, start_x: int = 0, start_y: int = 0,
                    goal_x: int = 0, goal_y: int = 0):  # noqa
        self._maze = maze
        self._start_x = start_x if start_x != 0 else 1
        self._start_y = start_y if start_y != 0 else 1
        self._goal_x = goal_x if goal_x != 0 else maze.shape[0] - 2
        self._goal_y = goal_y if goal_y != 0 else maze.shape[1] - 2
        self._maze[self._goal_x][self._goal_y] = 3
        self._frontier.clear()
        self._explored_states.clear()
        self._maze_type = maze_type
        self._steps_count = 0

    @abstractmethod
    def search_agent(self, show_visuals: bool = True):
        pass

    def _check_possible_moves(self, pos_x: int, pos_y: int, cost: int = 0, heuristic_function=None) -> int:  # noqa
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        possible_moves_count = 0
        for dx, dy in directions:
            if (Node(pos_x + dx, pos_y + dy, 0, 0) not in self._frontier
                    and (pos_x + dx, pos_y + dy) not in self._explored_states
                    and self._maze[pos_x + dx][pos_y + dy] != 1):
                if heuristic_function:
                    bisect.insort(self._frontier,
                                  Node(pos_x + dx, pos_y + dy, cost + 1,
                                       heuristic_function((pos_x + dx, pos_y + dy),
                                                          (self._goal_x, self._goal_y)) + cost + 1))
                else:
                    self._frontier.append(Node(pos_x + dx, pos_y + dy, 0, 0))
                possible_moves_count += 1
        return possible_moves_count

    def _set_state_as_explored(self, pos_x: int, pos_y: int):
        self._explored_states.append((pos_x, pos_y))
        self._maze[pos_x][pos_y] = 2

    def _visualize_maze(self):
        plt.clf()
        plt.title(str(self) + ' in maze ' + self._maze_type)
        plt.imshow(self._maze.transpose())
        plt.axis('off')
        plt.pause(0.0001)
        plt.draw()


class Node:
    def __init__(self, pos_x: int, pos_y: int, previous_cost: int, estimated_cost: int):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.previous_cost = previous_cost
        self.estimated_cost = estimated_cost

    def __lt__(self, other):
        return self.estimated_cost < other.estimated_cost

    def __eq__(self, other):
        return self.pos_x == other.pos_x and self.pos_y == other.pos_y
