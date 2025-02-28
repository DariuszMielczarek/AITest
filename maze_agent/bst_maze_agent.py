from abc import ABC, abstractmethod
from heapq import heappop

import numpy as np

from maze_agent.goal_exception import GoalException
from maze_agent.maze_agent import MazeAgent


class BstMazeAgent(MazeAgent):
    def search_agent(self):
        steps_count = 0
        while len(self._frontier) != 0:
            steps_count += 1
            (pos_x, pos_y) = self._frontier.pop(0)
            if pos_x == self._goal_x and pos_y == self._goal_y:
                return steps_count
            self._check_possible_moves(pos_x, pos_y)
            self._set_state_as_explored(pos_x, pos_y)
            self._visualize_maze()
        raise GoalException

