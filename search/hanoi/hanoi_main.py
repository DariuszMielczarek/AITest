from search.hanoi import Hanoi, HanoiAgent, DstHanoiAgent, BstHanoiAgent, IdsHanoiAgent, AStarHanoiAgent, \
    goal_tower_height_heuristic, goal_two_towers_height_heuristic, \
    goal_two_towers_and_diffs_sum_heuristic, goal_two_towers_and_diffs_max_heuristic, count_on_wrong_place, \
    count_all_moves


def test_hanoi_agent(agent: HanoiAgent, tests_count: int, show_visuals: bool = True, heuristic_function=None):
    try:
        results = []
        for game_size in range(1, tests_count + 1):
            hanoi_start = Hanoi(game_size, 2)
            hanoi_goal = Hanoi(game_size, 1)
            agent.reset_agent(hanoi_start, hanoi_goal)
            steps, cost = agent.search_agent(show_visuals, heuristic_function)
            print(str(agent) + ' found goal in ' + str(steps) + ' steps for game size = ' + str(game_size))
            results.append((steps, cost))
        return results
    except Exception as e:
        print('Exception in ' + str(agent) + ' usage: ' + str(e))


if __name__ == '__main__':
    test_count = 7

    # DST Agent
    hanoi_game_agent_dst: HanoiAgent = DstHanoiAgent()
    results_dst = test_hanoi_agent(hanoi_game_agent_dst, test_count, False)

    # BST Agent
    hanoi_game_agent_bst: HanoiAgent = BstHanoiAgent()
    results_bst = test_hanoi_agent(hanoi_game_agent_bst, test_count, False)

    # IDS Agent
    hanoi_game_agent_ids: HanoiAgent = IdsHanoiAgent()
    results_ids = test_hanoi_agent(hanoi_game_agent_ids, 7, False)

    # A-Star1 Agent
    hanoi_game_agent_a_star: HanoiAgent = AStarHanoiAgent()
    results_a_star1 = test_hanoi_agent(hanoi_game_agent_a_star, test_count, False, goal_tower_height_heuristic)

    # A-Star2 Agent
    hanoi_game_agent_a_star2: HanoiAgent = AStarHanoiAgent()
    results_a_star2 = test_hanoi_agent(hanoi_game_agent_a_star2, test_count, False, goal_two_towers_height_heuristic)

    # A-Star3 Agent
    hanoi_game_agent_a_star3: HanoiAgent = AStarHanoiAgent()
    results_a_star3 = test_hanoi_agent(hanoi_game_agent_a_star3, test_count, False,
                                       goal_two_towers_and_diffs_sum_heuristic)

    # A-Star4 Agent
    hanoi_game_agent_a_star4: HanoiAgent = AStarHanoiAgent()
    results_a_star4 = test_hanoi_agent(hanoi_game_agent_a_star4, test_count, False,
                                       goal_two_towers_and_diffs_max_heuristic)

    # A-Star5 Agent
    hanoi_game_agent_a_star5: HanoiAgent = AStarHanoiAgent()
    results_a_star5 = test_hanoi_agent(hanoi_game_agent_a_star5, test_count, False,
                                       count_on_wrong_place)

    # A-Star6 Agent
    hanoi_game_agent_a_star6: HanoiAgent = AStarHanoiAgent()
    results_a_star6 = test_hanoi_agent(hanoi_game_agent_a_star6, test_count, False,
                                       count_all_moves)

    print(results_dst)
    print(results_bst)
    print(results_ids)
    print(results_a_star1)
    print(results_a_star2)
    print(results_a_star3)
    print(results_a_star4)
    print(results_a_star5)
    print(results_a_star6)
