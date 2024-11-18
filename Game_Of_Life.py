import matplotlib.pyplot as plt

class GameOfLife(object):
    def __init__(self, x_dim, y_dim):
        self.rows = x_dim
        self.cols = y_dim
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def get_grid(self):
        return self.grid

    def set_grid(self, grid):
        self.grid = grid

    def print_grid(self):
        for row in self.grid:
            print(row)

    def populate_grid(self, coords):
        '''
            Populates the game grid with live cells at the specified coordinates.
            Parameters:
                coords: A list of tuples. Each tuple represents the (x, y) coordinates of a live cell.
        '''
        for coord in coords:
            if 0 <= coord[0] < self.rows and 0 <= coord[1] < self.cols:
                self.grid[coord[0]][coord[1]] = 1

    def count_neighbours(self, coord):
        # Count live neighbors with boundary checks
        '''
        :param coord:  A list of tuples. Each tuple represents the (x, y) coordinates of a live cell.
        :return: number of neighbours that are alive around the cell
        '''
        neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue  # Skip the cell itself
                nx, ny = coord[0] + i, coord[1] + j
                if 0 <= nx < self.rows and 0 <= ny < self.cols:  # Boundary check
                    neighbors += self.grid[nx][ny]
        return neighbors

    def make_step(self):
        # Create a new grid to store the next state
        ''''
        alive<2:Die
        alive>3:Die
        alive=2,3:Stay alive
        Dead=3:Alive
        :return: new grid with the next state'''
        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):
                neighbors = self.count_neighbours([i, j])
                if self.grid[i][j] == 1:  # Cell is alive
                    if neighbors < 2 or neighbors > 3:  # Under/Overpopulation
                        new_grid[i][j] = 0
                    else:
                        new_grid[i][j] = 1
                else:  # Cell is dead
                    if neighbors == 3:  # Reproduction
                        new_grid[i][j] = 1

        self.grid = new_grid

    def make_steps(self, steps):
        for _ in range(steps):
            self.make_step()
        return self.grid

    def draw_grid(self):
        for row in self.grid:
            print("-" * (self.cols * 3))
            for cell in row:
                if cell == 1:
                    print("X |", end="")
                else:
                    print("  |", end="")
            print()
        print("-" * (self.cols * 3))

    def draw_plot(self):
        fig, ax = plt.subplots(figsize=(6, 6))
        x, y, collor = [], [], []

        for i in range(self.rows):
            for j in range(self.cols):
                x.append(j)  # x-coordinate for each cell
                y.append(self.rows - i - 1)  # y-coordinate (inverted for display)
                if self.grid[i][j] == 1:
                    collor.append('red')  # Alive cells are red
                else:
                    collor.append('gray')  # Dead cells are gray

        # Scatter plot with colors for alive and dead cells
        ax.scatter(x, y, c=collor, s=500, edgecolors='gray', marker='s')
        ax.set_xlim(-0.5, self.cols - 0.5)
        ax.set_ylim(-0.5, self.rows - 0.5)
        ax.invert_yaxis()  # Invert y-axis to match printed grid

        # Display gridlines
        ax.set_xticks(range(self.cols))
        ax.set_yticks(range(self.rows))
        ax.grid(color='gray', linestyle='--', linewidth=0.5)

        # Display the plot
        plt.show()


# Create a Game of Life instance
game = GameOfLife(x_dim=30, y_dim=30)

# Populate grid with the blinker pattern
#game.populate_grid([(14, 15), (15, 15), (16, 15), (15, 14), (16, 16), (14, 16), (15, 17)])
game.populate_grid([(14, 16), (15, 16), (16, 16), (18, 16), (19, 16), (20, 16),
(16, 14), (16, 15), (16, 17), (16, 18),
(18, 14), (18, 15), (18, 17), (18, 18),
(14, 18), (15, 18), (16, 18), (18, 18), (19, 18), (20, 18)])

# Print initial grid
print("Initial Grid:")
game.print_grid()

# Visualize using scatter plot
print("\nScatter Plot of Initial Grid:")
game.draw_plot()

# Make a step and visualize again
n = int(input("Press Enter to make a step: "))
for i in range(1, n):
    print(f"\nScatter Plot After {i} Step:")
    game.make_step()
    game.draw_plot()

















