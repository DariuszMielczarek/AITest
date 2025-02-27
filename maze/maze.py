import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')


class Maze:
    _maze: np.ndarray

    def __init__(self, size_x: int, size_y: int, show_generation_steps: bool = False):
        self._maze = np.ones((size_x+2, size_y+2))
        self._dfs_generate_maze(1, 1, show_generation_steps)

    def _dfs_generate_maze(self, start_x: int, start_y: int, show_generation_steps: bool) -> None:

        self._maze[start_x][start_y] = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            if self._stop_generating_test():
                break
            if (1 <= dx + start_x < self._maze.shape[0] - 1 and 1 <= dy + start_y < self._maze.shape[1] - 1
                    and self._maze[dx + start_x, dy + start_y] != 0 and self._check_can_generate_new(start_x + dx, start_y + dy)):
                if show_generation_steps:
                    self._visualize_maze()
                self._dfs_generate_maze(start_x + dx, start_y + dy, show_generation_steps)

    def _check_can_generate_new(self, pos_x: int, pos_y: int) -> bool:
        counter = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            if self._maze[pos_x + dx][pos_y + dy] == 0:
                counter += 1

        return counter < 2

    def _stop_generating_test(self):
        return self._check_maze_empty_fields_to_walls_ratio() and self._check_if_goal_field_is_zero()

    def _check_if_goal_field_is_zero(self):
        return self._maze[-2, -2] == 0

    def _check_maze_empty_fields_to_walls_ratio(self) -> bool:
        return self._maze.sum() < 2*(self._maze.shape[0] * self._maze.shape[1]) / 3

    def _visualize_maze(self):
        plt.clf()
        plt.imshow(self._maze)
        plt.axis('off')
        plt.pause(0.01)
        plt.draw()

    def save_maze(self) -> str:
        pass
