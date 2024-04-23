from SearchAlgorithms import *


class Maze(Search):

    def __init__(self, filename):

        # Read file and set height and width of maze
        with open(filename) as f:
            contents = f.read()

        # Validate start and goal
        if contents.count("A") != 1:
            raise Exception("You can only have one starting point")
        elif contents.count("B") != 1:
            raise Exception("You can only have one target")

        # Determine height and width of maze
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        # Keep track of walls
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.target = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

        self.solution = None
        self.explored = None
        self.cost = None

    def neighbors(self, node):
        row, col = node.state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append(((r, c), action))
        return result

    def heuristic(self, state):
        state_row, state_col = state
        target_row, target_col = self.target
        return abs(state_row-target_row)+abs(state_col-target_col)

    def print(self):
        solution = self.solution[0] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.target:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print("")
        print("")

    def dfs_solve(self):
        res = Search.dfs(self, self.start, self.target)
        self.solution = (res[0], res[1])
        self.explored = res[2]

    def bfs_solve(self):
        res = Search.bfs(self, self.start, self.target)
        self.solution = (res[0], res[1])
        self.explored = res[2]

    def greedy_bfs_solve(self):
        res = Search.greedy_bfs(self, self.start, self.target)
        self.solution = (res[0], res[1])
        self.explored = res[2]

    def a_star_solve(self):
        res = Search.a_star(self, self.start, self.target)
        self.solution = (res[0], res[1])
        self.explored = res[2]
        self.cost = res[3]

    def print_image(self, filename, show_solution=True, show_explored=False):
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 50
        cell_border = 2

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.width * cell_size, self.height * cell_size),
            "black"
        )
        draw = ImageDraw.Draw(img)

        solution = self.solution[0] if self.solution is not None else None
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):

                # Walls
                if col:
                    fill = (40, 40, 40)
                    text = ""
                # Start
                elif (i, j) == self.start:
                    fill = (255, 0, 0)
                    text = ""

                # Goal
                elif (i, j) == self.target:
                    fill = (0, 171, 28)
                    text = ""

                # Solution
                elif solution is not None and show_solution and (i, j) in solution:
                    fill = (220, 235, 113)
                    text = f"{self.heuristic((i, j))}"
                    if self.cost is not None:
                        text += f"+{self.cost[(i,j)]}"

                # Explored
                elif solution is not None and show_explored and (i, j) in self.explored:
                    fill = (212, 97, 85)
                    text = f"{self.heuristic((i, j))}"
                    if self.cost is not None:
                        text += f"+{self.cost[(i, j)]}"

                # Empty cell
                else:
                    fill = (237, 240, 252)
                    text = f"{self.heuristic((i, j))}"

                # Draw cell
                draw.rectangle(
                    ([(j * cell_size + cell_border, i * cell_size + cell_border),
                        ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                    fill=fill
                )
                if self.cost is not None and (i, j) in self.cost:
                    x = j * cell_size + cell_border
                else:
                    x = (j * cell_size + cell_border + (j + 1) * cell_size - cell_border) / 2
                y = (i * cell_size + cell_border + (i + 1) * cell_size - cell_border) / 2
                draw.text(
                    (x, y),
                    text=text, font=ImageFont.truetype("Rubik-Medium_3.ttf", 16), align="center", fill="black"
                )

        img.save(filename)
