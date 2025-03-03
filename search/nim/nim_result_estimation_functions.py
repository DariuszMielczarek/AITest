from search.nim import Nim


def no_winner_function():
    return 0


def even_total_discs_function(nim: Nim):
    total_discs = sum(nim.towers)
    start_sum = sum(Nim(len(nim.towers)).towers)
    if total_discs == 2 and max(nim.towers) == 1:
        return -1
    elif total_discs == 2:
        return 1
    if total_discs == 2 * max(nim.towers) == 2 * min(nim.towers):
        return 1
    if total_discs % 2 == 0:
        return 1 - (total_discs / start_sum)
    else:
        return 0 - (total_discs / start_sum)
