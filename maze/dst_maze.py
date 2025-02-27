import random
from maze import Maze


class DstMaze(Maze):
    def _generate_maze(self, start_x: int, start_y: int, show_generation_steps: bool) -> None:
        self._maze[start_x][start_y] = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            if self._stop_generating_test():
                break
            if (1 <= dx + start_x < self._maze.shape[0] - 1 and 1 <= dy + start_y < self._maze.shape[1] - 1
                    and self._maze[dx + start_x, dy + start_y] != 0
                    and self._check_can_generate_new(start_x + dx, start_y + dy)):
                if show_generation_steps:
                    self._visualize_maze()
                self._generate_maze(start_x + dx, start_y + dy, show_generation_steps)

    def _stop_generating_test(self):
        return self._check_maze_empty_fields_to_walls_ratio() and self._check_if_goal_field_is_reachable()

    def _check_if_goal_field_is_reachable(self):
        return self._maze[-2, -3] == 0 or self._maze[-3, -2] == 0

    def _check_maze_empty_fields_to_walls_ratio(self) -> bool:
        return self._maze.sum() < 2 * (self._maze.shape[0] * self._maze.shape[1]) / 3
