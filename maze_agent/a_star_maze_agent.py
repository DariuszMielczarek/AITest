from maze_agent.goal_exception import GoalException
from maze_agent.heuristics import manhattan_distance
from maze_agent.maze_agent import MazeAgent, Node


class AStarMazeAgent(MazeAgent):
    def search_agent(self, show_visuals: bool = True):
        node = Node(self._start_x, self._start_y, 0,
                    manhattan_distance((self._start_x, self._start_y), (self._goal_x, self._goal_y)))
        self._frontier.append(node)
        while len(self._frontier) != 0:
            self._steps_count += 1
            node = self._frontier.pop(0)
            if node.pos_x == self._goal_x and node.pos_y == self._goal_y:
                return self._steps_count
            self._check_possible_moves(node.pos_x, node.pos_y, node.previous_cost, manhattan_distance)
            self._set_state_as_explored(node.pos_x, node.pos_y)
            if show_visuals:
                self._visualize_maze()
        raise GoalException

    def __str__(self):
        return "A-Star Agent"
