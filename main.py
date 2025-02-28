from maze import Maze, DstMaze, AStarMaze
from maze_agent import MazeAgent, BstMazeAgent, DstMazeAgent, IdsMazeAgent


def test_agent(agent: MazeAgent, show_visuals: bool = True):
    dst_maze: Maze = Maze(filename='dst_maze.npy')
    a_star_maze: Maze = Maze(filename='a_star_maze.npy')
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


if __name__ == '__main__':
    # size = 25
    # maze: Maze = DstMaze(size_x=size, size_y=size, show_generation_steps=False)
    # maze.save_maze('dst_maze')
    # maze2: Maze = AStarMaze(size_x=size, size_y=size, show_generation_steps=True)
    # maze2.save_maze('a_star_maze')
    # BST Agent
    maze_agent_bst: MazeAgent = BstMazeAgent()
    test_agent(maze_agent_bst, show_visuals=False)

    # DST Agent
    maze_agent_dst: MazeAgent = DstMazeAgent()
    test_agent(maze_agent_dst, show_visuals=False)

    # IDS Agent
    maze_agent_ids: MazeAgent = IdsMazeAgent()
    test_agent(maze_agent_ids, show_visuals=False)
