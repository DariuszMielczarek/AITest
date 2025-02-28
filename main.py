from maze import Maze, DstMaze, AStarMaze
from maze_agent import MazeAgent, BstMazeAgent

if __name__ == '__main__':
    size = 25
    # maze: Maze = DstMaze(size_x=size, size_y=size, show_generation_steps=False)
    # maze.save_maze('dst_maze')
    # maze2: Maze = AStarMaze(size_x=size, size_y=size, show_generation_steps=True)
    # maze2.save_maze('a_star_maze')
    dst_maze: Maze = Maze(filename='dst_maze.npy')
    a_star_maze: Maze = Maze(filename='a_star_maze.npy')
    maze_agent_bst: MazeAgent = BstMazeAgent(dst_maze.get_maze())
    try:
        bst_result = maze_agent_bst.search_agent()
        print('BST agent found goal in ' + str(bst_result) + ' steps for DST maze')
    except Exception as e:
        print('Exception in BST agent usage for DST maze: ' + str(e))
    maze_agent_bst.change_maze(a_star_maze.get_maze())
    try:
        bst_result = maze_agent_bst.search_agent()
        print('BST agent found goal in ' + str(bst_result) + ' steps for A-Star maze')
    except Exception as e:
        print('Exception in BST agent usage for A-Star maze: ' + str(e))
