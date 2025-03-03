from abc import abstractmethod
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')


class Maze:
    _maze: np.ndarray

    def __init__(self, filename: str = None, size_x: int = 0, size_y: int = 0, show_generation_steps: bool = False):
        if filename:
            self.load_maze(filename)
        else:
            if size_x <= 0 or size_y <= 0:
                raise ValueError('Size must be greater than zero')
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

    def _visualize_maze(self) -> None:
        plt.clf()
        plt.imshow(self._maze.transpose())
        plt.axis('off')
        plt.pause(0.01)
        plt.draw()

    def save_maze(self, filename) -> str:
        np.save(filename, self._maze)
        return filename

    def load_maze(self, filename) -> None:
        self._maze = np.load(filename)

    def display_maze(self) -> None:
        plt.clf()
        plt.imshow(self._maze.transpose())
        plt.axis('off')
        plt.show()

    def get_maze(self) -> np.ndarray:
        return self._maze
