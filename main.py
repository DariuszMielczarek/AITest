from hanoi import Hanoi, HanoiAgent, DstHanoiAgent, BstHanoiAgent, IdsHanoiAgent
from maze import Maze, DstMaze, AStarMaze
from maze_agent import MazeAgent, BstMazeAgent, DstMazeAgent, IdsMazeAgent, AStarMazeAgent


def test_agent(agent: MazeAgent, show_visuals: bool = True):
    dst_maze: Maze = Maze(filename='dst_maze_mini.npy')
    a_star_maze: Maze = Maze(filename='a_star_maze_mini.npy')
    agent.change_maze(dst_maze.get_maze(), 'DST')
    try:
        result = agent.search_agent(show_visuals)
        print(str(agent) + ' found goal in ' + str(result) + ' steps for DST maze')
    except Exception as e:
        print('Exception in ' + str(agent) + ' usage for DST maze: ' + str(e))
    agent.change_maze(a_star_maze.get_maze(), 'A-Star')
    try:
        result = agent.search_agent(show_visuals)
        print(str(agent) + ' found goal in ' + str(result) + ' steps for A-Star maze')
    except Exception as e:
        print('Exception in ' + str(agent) + ' usage for A-Star maze: ' + str(e))


def test_hanoi_agent(agent: HanoiAgent, tests_count: int, show_visuals: bool = True):
    try:
        for game_size in range(1, tests_count+1):
            hanoi_start = Hanoi(game_size, 2)
            hanoi_goal = Hanoi(game_size, 1)
            agent.reset_agent(hanoi_start, hanoi_goal)
            result = agent.search_agent(show_visuals)
            print(str(agent) + ' found goal in ' + str(result) + ' steps for game size = ' + str(game_size))
    except Exception as e:
        print('Exception in ' + str(agent) + ' usage: ' + str(e))


if __name__ == '__main__':
    # size = 10
    # # maze: Maze = DstMaze(size_x=size, size_y=size, show_generation_steps=True)
    # # maze.save_maze('dst_maze_mini')
    # maze2: Maze = AStarMaze(size_x=size, size_y=size, show_generation_steps=True)
    # maze2.save_maze('a_star_maze_mini')
    # # BST Agent
    # maze_agent_bst: MazeAgent = BstMazeAgent()
    # test_agent(maze_agent_bst, show_visuals=False)
    #
    # # DST Agent
    # maze_agent_dst: MazeAgent = DstMazeAgent()
    # test_agent(maze_agent_dst, show_visuals=False)
    #
    # # IDS Agent
    # maze_agent_ids: MazeAgent = IdsMazeAgent()
    # test_agent(maze_agent_ids, show_visuals=False)
    #
    # # A-Star Agent
    # maze_agent_a_star: MazeAgent = AStarMazeAgent()
    # test_agent(maze_agent_a_star, show_visuals=True)

    # DST Agent
    hanoi_game_agent_dst: HanoiAgent = DstHanoiAgent()
    test_hanoi_agent(hanoi_game_agent_dst, 6, False)

    # BST Agent
    hanoi_game_agent_bst: HanoiAgent = BstHanoiAgent()
    test_hanoi_agent(hanoi_game_agent_bst, 6, False)

    # IDS Agent
    hanoi_game_agent_ids: HanoiAgent = IdsHanoiAgent()
    test_hanoi_agent(hanoi_game_agent_ids, 3, True)
