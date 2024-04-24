# python3 dfs.py --mazeFile=maze_20.csv

import argparse 
import time 
import random
import pygame
import numpy as np

from dfsClasses import DFS

black = (44,43,42)          # 0: wall colors
grey = (219, 218, 219)      # 1: Unsearched nodes
green = (22,255,33)         # 2: start node
red = (254,8,20)            # 3: goal node
orange = (255, 174, 82)     # 4: visited nodes
maroon = (136, 56, 76)      # 5: returned solution path
yellow = (239, 249, 40)     # 6: frontier nodes


colorsList = [black, grey, green, red, orange, maroon, yellow]

if __name__ == "__main__":

    ''' Testing stuff
    print("length of grid= " + str(len(grid)))
    print("num of columns= " + str(len(grid[0])))

    print("start position: " + str(start_pos))
    print("goal position: " + str(goal_pos))
    print(gridDimension)

    print(grid)

    '''


    # parsing user input
    # example: python3 dfs.py --mazeFile=maze_20.csv
    mazeString = "maze_"
    mazeNum = random.randint(1,30)
    mazeNum-=1

    randomMaze = mazeString + str(mazeNum) + ".csv"

    parser = argparse.ArgumentParser()
    parser.add_argument("--mazeFile", help="filename (csv) of the maze to load.", default=randomMaze, type=str)
    args = parser.parse_args()

    startTime = time.time()

    mazeAddress = "mazes/" + args.mazeFile
    grid = np.genfromtxt(mazeAddress, delimiter=',').astype(np.int64)

    numRows = len(grid)
    numColumns = len(grid[0])

    # Start position will always be top left
    startPosition = (0,0)

    #goal position will always be bottom right
    goalPosition = (numRows-1, numColumns-1)

    # Changing g
    grid[0, 0] = 2      # start = 2
    grid[-1, -1] = 3    # goal = 3
    gridDimension = (numRows-1, numColumns-1)

    # size of each tile 
    width = height = 18
    screenSize = [739,739]

    pygame.init()
    pygame.display.set_caption(f"DFS Pathfinding on: {args.mazeFile}")
    screen = pygame.display.set_mode(screenSize)


    done = False
    running = False
    closeWindow = False

    # FPS manager
    clock = pygame.time.Clock() 