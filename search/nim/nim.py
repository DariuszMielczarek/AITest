import copy


class Nim:
    def __init__(self, n=5, towers=None):
        if towers is not None:
            self.towers = copy.deepcopy(towers)
        else:
            self.towers = []
            for i in range(0, n):
                self.towers.append(1+i*2)

    def get_possible_moves(self):
        possible_moves = []
        for tower_number in range(len(self.towers)):
            for elements_count in range(1, self.towers[tower_number] + 1):
                possible_moves.append((tower_number, elements_count))
        return possible_moves

    def move(self, tower_number, elements_count):
        self.towers[tower_number] -= elements_count

    def visualize_game(self):
        for tower_number in range(len(self.towers)):
            print(f'Tower {tower_number+1} has {self.towers[tower_number]} element(s)')

    def __eq__(self, other):
        return self.towers == other.towers

    def __hash__(self):
        return hash(tuple(self.towers))
