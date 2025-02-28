from maze_agent.goal_exception import GoalException
from maze_agent.maze_agent import MazeAgent


class DstMazeAgent(MazeAgent):
    def search_agent(self, show_visuals: bool = True):
        while len(self._frontier) != 0:
            self._steps_count += 1
            (pos_x, pos_y) = self._frontier.pop()
            if pos_x == self._goal_x and pos_y == self._goal_y:
                return self._steps_count
            self._check_possible_moves(pos_x, pos_y)
            self._set_state_as_explored(pos_x, pos_y)
            if show_visuals:
                self._visualize_maze()
        raise GoalException

    def __str__(self):
        return "DST Agent"

