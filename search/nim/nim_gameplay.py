from search.nim import Nim
from search.nim.nim_agent import NimAgent


class NimGameplay:
    @staticmethod
    def gameplay(nim: Nim, agent: NimAgent, estimating_function):
        move = 0
        while sum(nim.towers) != 0:
            move += 1
            if move % 2 == 1:
                possible_moves = nim.get_possible_moves()
                while True:
                    count = int(input('Remove count: '))
                    tower = int(input('From tower number: '))
                    if (tower-1, count) in possible_moves:
                        break
                nim.move(tower-1, count)
                print(f'PLAYER TURN: Remove {count} from {tower}')
                nim.visualize_game()
            else:
                agent.reset_agent(nim)
                tower, count = agent.search_agent(False, estimating_function, False)
                nim.move(tower, count)
                print(str(agent) + f' TURN: Remove {count} from {tower+1}')
                nim.visualize_game()
        return ('PLAYER WON' if move % 2 == 1 else str(agent) + ' WON') + f' IN {move} MOVES'
