from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')

import numpy as np


class MazeAgent(ABC):
    _maze: np.ndarray
    _start_x: int
    _start_y: int
    _goal_x: int
    _goal_y: int
    _frontier: list = []
    _explored_states: list = []

    def __init__(self, maze: np.ndarray, start_x: int = 0, start_y: int = 0, goal_x: int = 0, goal_y: int = 0):
        self.change_maze(maze, start_x, start_y, goal_x, goal_y)

    def change_maze(self, maze: np.ndarray, start_x: int = 0, start_y: int = 0, goal_x: int = 0, goal_y: int = 0):
        self._maze = maze
        self._start_x = start_x if start_x != 0 else 1
        self._start_y = start_y if start_y != 0 else 1
        self._goal_x = goal_x if goal_x != 0 else maze.shape[0] - 2
        self._goal_y = goal_y if goal_y != 0 else maze.shape[1] - 2
        self._maze[self._goal_x][self._goal_y] = 3
        self._frontier.clear()
        self._explored_states.clear()
        self._frontier.append((self._start_x, self._start_y))

    @abstractmethod
    def search_agent(self):
        pass

    def _check_possible_moves(self, pos_x: int, pos_y: int):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            if ((pos_x + dx, pos_y + dy) not in self._frontier
                    and (pos_x + dx, pos_y + dy) not in self._explored_states
                    and self._maze[pos_x + dx][pos_y + dy] != 1):
                self._frontier.append((pos_x + dx, pos_y + dy))

    def _set_state_as_explored(self, pos_x: int, pos_y: int):
        self._explored_states.append((pos_x, pos_y))
        self._maze[pos_x][pos_y] = 2

    def _visualize_maze(self):
        plt.clf()
        plt.imshow(self._maze.transpose())
        plt.axis('off')
        plt.pause(0.02)
        plt.draw()
