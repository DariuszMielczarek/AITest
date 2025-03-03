import bisect
import copy

from search.maze.maze_agent.goal_exception import GoalException
from search.nim.nim_agent import NimState, NimAgent


class BstNimAgent(NimAgent):
    def search_agent(self, show_visuals: bool = True, heuristic_function=None, opponent_starts=False):
        start_nim = self._nim_start_state
        if opponent_starts:
            possible_nims = self._check_possible_moves(start_nim)
            for nim in possible_nims:
                new_nim, tower, count = self._sim_opponent_move_random(nim)
                moves = [('O', tower, count)]
                if heuristic_function:
                    bisect.insort(self._frontier, NimState(new_nim, 0, heuristic_function(new_nim), moves))
                else:
                    self._frontier.append(NimState(new_nim, 0, 0, moves))
        else:
            self._frontier.append(NimState(start_nim, 0, 0, []))
        while len(self._frontier) != 0:
            self._steps_count += 1
            state = self._frontier.pop(0)
            if state.nim == self._nim_goal_state:
                if show_visuals:
                    print(f'PLAYER WON!\nSTEP {self._steps_count} (FINAL), COST {state.previous_cost}:')
                    state.visualize_game()
                return state.moves[0][1], state.moves[0][2]
            possible_moves = self._check_possible_moves(state.nim)
            for nim, tower_player, count_player in possible_moves:
                if nim == self._nim_goal_state:
                    if show_visuals:
                        print(f'PLAYER WON!\nSTEP {self._steps_count} (FINAL), COST {state.previous_cost}:')
                        state.visualize_game()
                    if len(state.moves) == 0:
                        return tower_player, count_player
                    else:
                        return state.moves[0][1], state.moves[0][2]
                new_nim, tower, count = self._sim_opponent_move_random(nim)
                if new_nim == self._nim_goal_state:
                    if show_visuals:
                        print(f'OPPONENT WON!\nSTEP {self._steps_count} (FINAL), COST {state.previous_cost}:')
                        state.visualize_game()
                if new_nim not in self._explored_states and NimState(new_nim, 0, 0, []) not in self._frontier:
                    new_moves = copy.deepcopy(state.moves)
                    new_moves.append(('P', tower_player, count_player))
                    new_moves.append(('O', tower, count))
                    if heuristic_function:
                        bisect.insort(self._frontier, NimState(new_nim, state.previous_cost + 1,
                                                               heuristic_function(new_nim) + state.previous_cost + 1,
                                                               new_moves))
                    else:
                        self._frontier.append(NimState(new_nim, state.previous_cost + 1, 0, new_moves))
            self._set_state_as_explored(state.nim)
            if show_visuals:
                print(f'STEP {self._steps_count}, COST {state.previous_cost}:')
                state.visualize_game()
        raise GoalException

    def __str__(self):
        return "BST Agent"
