import numpy as np
with open("day08/input.txt") as file:
    input = list([i for i in file.read().strip().split()])

# store data as a grid
grid = [list(map(int, list(tree)))for tree in input]
forest = np.array(grid)
visibleTrees = 0

# go thorugh every position and check if visible by checking all directions
y = len(forest)  # height
x = len(forest[0])  # width

for i in range(y):
    for j in range(x):
        currentTree = forest[i][j]
        if j == 0 or i == 0:  # check side edges
            visibleTrees += 1
        elif np.amax(forest[i, :j]) < currentTree:  # check all left
            visibleTrees += 1
        # check all right and right edge
        elif j == x-1 or np.amax(forest[i, (j+1):]) < currentTree:
            visibleTrees += 1
        elif np.amax(forest[:i, j]) < currentTree:  # check all up
            visibleTrees += 1
        # check all down and down edge
        elif i == y-1 or np.amax(forest[(i+1):, j]) < currentTree:
            visibleTrees += 1

print(visibleTrees)

# https://www.geeksforgeeks.org/numpy-amax-python/
