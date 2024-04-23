from Maze import *


if __name__ == '__main__':
    for num in range(1, 4):
        m = Maze(f"maze{num}.txt")
        m.dfs_solve()
        m.print_image(f"maze{num}dfs.png", show_explored=True)
        m.bfs_solve()
        m.print_image(f"maze{num}bfs.png", show_explored=True)
        m.greedy_bfs_solve()
        m.print_image(f"maze{num}greedy_bfs.png", show_explored=True)
        m.a_star_solve()
        m.print_image(f"maze{num}A_star.png", show_explored=True)
