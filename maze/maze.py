from abc import ABC, abstractmethod
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')


class Maze(ABC):
    _maze: np.ndarray

    def __init__(self, size_x: int, size_y: int, show_generation_steps: bool = False):
        self._maze = np.ones((size_x + 2, size_y + 2))
        self._maze[size_x][size_y] = 0
        self._generate_maze(1, 1, show_generation_steps)

    @abstractmethod
    def _generate_maze(self, start_x: int, start_y: int, show_generation_steps: bool) -> None:
        pass

    def _check_can_generate_new(self, pos_x: int, pos_y: int) -> bool:
        if (pos_x == self._maze.shape[0] - 3 and pos_y == self._maze.shape[1] - 2
                or pos_x == self._maze.shape[0] - 2 and pos_y == self._maze.shape[1] - 3):
            return True
        counter = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            if self._maze[pos_x + dx][pos_y + dy] == 0:
                counter += 1

        return counter < 2

    def _visualize_maze(self):
        plt.clf()
        plt.imshow(self._maze.transpose())
        plt.axis('off')
        plt.pause(0.01)
        plt.draw()

    def save_maze(self) -> str:
        pass
