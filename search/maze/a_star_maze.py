from heapq import heappush, heappop
import random
from search.maze import Maze


class AStarMaze(Maze):
    def _generate_maze(self, start_x: int, start_y: int, show_generation_steps: bool) -> None:
        nodes_list: list[Node] = []
        self._maze[start_x][start_y] = 0

        heappush(nodes_list, Node(self._heuristic(start_x, start_y), 0, (start_x, start_y)))

        while len(nodes_list) != 0:
            if self._stop_generating_test():
                break
            read_node = heappop(nodes_list)
            node = read_node
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            random.shuffle(directions)

            for dx, dy in directions:
                if (1 <= dx + node.position[0] < self._maze.shape[0] - 1
                        and 1 <= dy + node.position[1] < self._maze.shape[1] - 1
                        and self._maze[dx + node.position[0], dy + node.position[1]] != 0
                        and self._check_can_generate_new_a_star(node.position[0] + dx, node.position[1] + dy,
                                                                node.position[0] + dx * 2, node.position[1] + dy * 2)):
                    if show_generation_steps:
                        self._visualize_maze()
                    self._maze[dx + node.position[0], dy + node.position[1]] = 0

                    new_node = Node(self._heuristic(dx + node.position[0], dy + node.position[1]),
                                    node.current_cost + 1, (dx + node.position[0], dy + node.position[1]))
                    if new_node not in nodes_list:
                        heappush(nodes_list, new_node)
                    if show_generation_steps:
                        self._visualize_maze()

    def _manhattan_heuristic(self, pos_x: int, pos_y: int) -> int:
        return (self._maze.shape[0] - 2 - pos_x) + (self._maze.shape[1] - 2 - pos_y)

    def _heuristic(self, pos_x: int, pos_y: int) -> int:
        neighbourhood_factor = 4
        manhattan_heuristic_value = self._manhattan_heuristic(pos_x, pos_y)
        min_x = 1 if pos_x < 4 else pos_x - 3
        min_y = 1 if pos_y < 4 else pos_y - 3
        max_x = self._maze.shape[0] - 1 if pos_x > self._maze.shape[0] - 4 else pos_x + 3
        max_y = self._maze.shape[1] - 1 if pos_y > self._maze.shape[1] - 4 else pos_y + 3
        maze_neighbourhood = self._maze[min_x:max_x + 1, min_y:max_y + 1]
        neighbourhood_size = maze_neighbourhood.shape[0] * maze_neighbourhood.shape[1]
        neighbourhood_size_penalty = 49 - neighbourhood_size
        return manhattan_heuristic_value + (
                neighbourhood_size - maze_neighbourhood.sum() + neighbourhood_size_penalty // 2) * neighbourhood_factor

    def _check_can_generate_new_a_star(self, pos_x: int, pos_y: int, next_x: int, next_y: int) -> bool:
        if (pos_x == self._maze.shape[0] - 3 and pos_y == self._maze.shape[1] - 2
                or pos_x == self._maze.shape[0] - 2 and pos_y == self._maze.shape[1] - 3):
            return True
        counter = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            if self._maze[pos_x + dx][pos_y + dy] == 0 and (pos_x + dx != next_x or pos_y + dy != next_y):
                counter += 1

        return counter < 2

    def _stop_generating_test(self):
        return self._check_maze_empty_fields_to_walls_ratio() and self._check_if_goal_field_is_reachable()

    def _check_if_goal_field_is_reachable(self):
        return self._maze[-2, -3] == 0 or self._maze[-3, -2] == 0

    def _check_maze_empty_fields_to_walls_ratio(self) -> bool:
        return self._maze.sum() < 2 * (self._maze.shape[0] * self._maze.shape[1]) / 3


class Node:
    def __init__(self, heuristic_value: int, current_cost: int, position: (int, int)):
        self.heuristic_value = heuristic_value
        self.current_cost = current_cost
        self.position = position

    def __lt__(self, other):
        return self.heuristic_value + self.current_cost < other.heuristic_value + other.current_cost

    def __str__(self):
        return f'Position ({str(self.position)}) and priority {self.current_cost + self.heuristic_value}'

    def __eq__(self, other):
        return self.position == other.position
