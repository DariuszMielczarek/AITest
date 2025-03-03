class Hanoi:
    def __init__(self, n, tower_number):
        self.towers = [[], [], []]
        self.towers[tower_number] = list(range(1, n + 1))
        self.n = n

    def get_possible_moves(self):
        possible_moves = []
        for tower_number in range(len(self.towers)):
            if len(self.towers[tower_number]) > 0:
                value = self.towers[tower_number][0]
                for tower_number2 in range(len(self.towers)):
                    if tower_number != tower_number2:
                        if len(self.towers[tower_number2]) == 0:
                            possible_moves.append((tower_number, tower_number2))
                        else:
                            value2 = self.towers[tower_number2][0]
                            if value < value2:
                                possible_moves.append((tower_number, tower_number2))
        return possible_moves

    def move(self, tower_number_from, tower_number_to):
        value = self.towers[tower_number_from].pop(0)
        self.towers[tower_number_to].insert(0, value)

    def visualize_game(self):
        for tower_number in range(len(self.towers)):
            print(f'{tower_number+1}: {self.towers[tower_number]}')

    def __eq__(self, other):
        return self.towers == other.towers
