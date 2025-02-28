from maze_agent.goal_exception import GoalException
from maze_agent.maze_agent import MazeAgent, Node


class IdsMazeAgent(MazeAgent):
    def search_agent(self, show_visuals: bool = True):
        self._frontier.append(Node(self._start_x, self._start_y, 0, 0))
        for limit in range(0, 1000):
            self._reset_maze()
            return_value = self._ids_search_agent((self._start_x, self._start_y), limit, show_visuals)
            if return_value:
                return return_value
        raise GoalException

    def _ids_search_agent(self, node: tuple, limit: int, show_visuals: bool = True):
        if limit == 0:
            if node[0] == self._goal_x and node[1] == self._goal_y:
                return self._steps_count
        else:
            self._steps_count += 1
            possible_neighbours = self._check_possible_moves(node[0], node[1])
            self._set_state_as_explored(node[0], node[1])
            if show_visuals:
                self._visualize_maze()
            while possible_neighbours > 0:
                node = self._frontier.pop()
                return_value = self._ids_search_agent((node.pos_x, node.pos_y), limit-1, show_visuals)
                if return_value:
                    return return_value
                possible_neighbours -= 1

    def _reset_maze(self):
        self._maze[self._maze == 2] = 0
        self._explored_states.clear()

    def __str__(self):
        return "IDS Agent"
