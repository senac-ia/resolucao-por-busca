# create maze generator

import random
import sys

# create a maze
def create_maze(width, height):
    maze = []
    for i in range(height):
        maze.append([])
        for j in range(width):
            maze[i].append(" ")
    return maze

# print maze
def print_maze(maze):
    for i in maze:
        for j in i:
            sys.stdout.write(str(j))
        print("")
    print("")
    return


# create a maze with a path
def create_maze_with_path(width, height):
    maze = create_maze(width, height)
    maze[0][0] = 1
    maze[height-1][width-1] = 1
    return maze
    
m = create_maze_with_path(10, 10)
print_maze(m)