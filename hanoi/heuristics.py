from hanoi import Hanoi


def goal_tower_height_heuristic(hanoi: Hanoi):
    return hanoi.n - len(hanoi.towers[1])


def goal_two_towers_height_heuristic(hanoi: Hanoi):
    return hanoi.n - len(hanoi.towers[1]) + len(hanoi.towers[2])


def goal_two_towers_and_diffs_sum_heuristic(hanoi: Hanoi):
    differences = 0
    for tower in hanoi.towers:
        for i in range(1, len(tower)):
            differences += tower[i] - tower[i - 1]
    return (hanoi.n - len(hanoi.towers[1]) + len(hanoi.towers[2])) + differences


def goal_two_towers_and_diffs_max_heuristic(hanoi: Hanoi):
    differences = 0
    for tower in hanoi.towers:
        for i in range(1, len(tower)):
            max_diff = 0
            diff = tower[i] - tower[i - 1]
            if diff > max_diff:
                max_diff = diff
            if i == len(tower) - 1:
                differences += max_diff
    return (hanoi.n - len(hanoi.towers[1]) + len(hanoi.towers[2])) + differences


def count_on_wrong_place(hanoi: Hanoi):
    count = 0
    for i in range(len(hanoi.towers)):
        for j in range(len(hanoi.towers[i])-1, -1, -1):
            if i == 1:
                if hanoi.towers[i][j] != hanoi.n - len(hanoi.towers[i]) + j + 1:
                    count += 1
            else:
                count += 1
    return count


def count_all_moves(hanoi: Hanoi):
    moves = 0
    for i in range(len(hanoi.towers)):
        for j in range(len(hanoi.towers[i])-1, -1, -1):
            if i == 1:
                if hanoi.towers[i][j] != hanoi.n - len(hanoi.towers[i]) + j + 1:
                    moves += (j + 1) ** 2
            else:
                moves += j + 1
    return moves
