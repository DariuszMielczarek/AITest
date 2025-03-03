from search.maze.maze_agent.goal_exception import GoalException
from search.maze.maze_agent.maze_agent import MazeAgent, Node


class DstMazeAgent(MazeAgent):
    def search_agent(self, show_visuals: bool = True):
        self._frontier.append(Node(self._start_x, self._start_y, 0, 0))
        while len(self._frontier) != 0:
            self._steps_count += 1
            node = self._frontier.pop()
            if node.pos_x == self._goal_x and node.pos_y == self._goal_y:
                return self._steps_count
            self._check_possible_moves(node.pos_x, node.pos_y)
            self._set_state_as_explored(node.pos_x, node.pos_y)
            if show_visuals:
                self._visualize_maze()
        raise GoalException

    def __str__(self):
        return "DST Agent"

