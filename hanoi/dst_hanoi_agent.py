from hanoi.hanoi_agent import HanoiAgent, HanoiState
from maze_agent.goal_exception import GoalException


class DstHanoiAgent(HanoiAgent):
    def search_agent(self, show_visuals: bool = True, heuristic_function=None):
        self._frontier.append(HanoiState(self._hanoi_start_state, 0, 0))
        while len(self._frontier) != 0:
            self._steps_count += 1
            state = self._frontier.pop()
            if state.hanoi == self._hanoi_goal_state:
                if show_visuals:
                    print(f'STEP {self._steps_count} (FINAL):')
                    state.hanoi.visualize_game()
                print(f'Result have cost = {state.previous_cost}')
                return self._steps_count, state.previous_cost
            self._check_possible_moves(state.hanoi, state.previous_cost)
            self._set_state_as_explored(state.hanoi)
            if show_visuals:
                print(f'STEP {self._steps_count}:')
                state.hanoi.visualize_game()
        raise GoalException

    def __str__(self):
        return "DST Agent"

