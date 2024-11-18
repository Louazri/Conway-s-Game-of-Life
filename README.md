# Conway's Game of Life

This project implements Conway's Game of Life, a cellular automaton devised by the British mathematician John Horton Conway in 1970. The game simulates the evolution of a grid of cells based on a set of simple rules, which determine whether each cell survives, dies, or reproduces in the next generation.

## Features

- **Grid Initialization**: Create a grid with a specified number of rows and columns.
- **Population**: Populate the grid with live cells.
- **Simulation**: Simulate one or more generations based on the rules of Conway's Game of Life.
- **Visualization**: Visualize the grid using a scatter plot to display live cells.

## Rules of Conway's Game of Life

Each cell on the grid can either be **alive** (1) or **dead** (0). The next generation of cells is determined by the following rules:
1. Any live cell with fewer than two live neighbors dies (underpopulation).
2. Any live cell with two or three live neighbors lives on to the next generation (survival).
3. Any live cell with more than three live neighbors dies (overpopulation).
4. Any dead cell with exactly three live neighbors becomes a live cell (reproduction).

## Installation

### Prerequisites
To run this project, you need Python 3 and the following libraries:
- `numpy`
- `matplotlib`

You can install the required libraries by running:

```bash
pip install numpy matplotlib
