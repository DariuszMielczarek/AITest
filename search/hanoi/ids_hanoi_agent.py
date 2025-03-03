from search.hanoi import HanoiAgent, HanoiState
from search.maze.maze_agent.goal_exception import GoalException


class IdsHanoiAgent(HanoiAgent):
    def search_agent(self, show_visuals: bool = True, heuristic_function=None):
        self._frontier.append(HanoiState(self._hanoi_start_state, 0, 0))
        for limit in range(0, 1000):
            self._explored_states.clear()
            return_value = self._ids_search_agent(
                HanoiState(self._hanoi_start_state, 0, 0), limit, show_visuals)
            if return_value:
                return return_value[0], return_value[1]
        raise GoalException

    def _ids_search_agent(self, state: HanoiState, limit: int, show_visuals: bool = True):
        if limit == 0:
            if state.hanoi == self._hanoi_goal_state:
                if show_visuals:
                    print(f'STEP {self._steps_count} (FINAL):')
                    state.hanoi.visualize_game()
                print(f'Result have cost = {state.previous_cost}')
                return self._steps_count, state.previous_cost
        else:
            self._steps_count += 1
            possible_neighbours = self._check_possible_moves(state.hanoi, state.previous_cost)
            self._set_state_as_explored(state.hanoi)
            if show_visuals:
                print(f'STEP {self._steps_count}:')
                state.hanoi.visualize_game()
            while possible_neighbours > 0:
                state = self._frontier.pop()
                return_value = self._ids_search_agent(state, limit - 1, show_visuals)
                if return_value:
                    return return_value[0], return_value[1]
                possible_neighbours -= 1

    def __str__(self):
        return "IDS Agent"
