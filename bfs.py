# python3 bfs.py --mazeFile=maze_1.csv

# TODO: Print size of solution after it is found

import time, csv, argparse
import pygame
import numpy as np

from classes import BFS , Queue, Node, isValidMove

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

    startTime = time.time()

    # parsing user input
    # example: python3 bfs.py --mazeFile=maze_1.csv
    parser = argparse.ArgumentParser()
    parser.add_argument("--mazeFile", help="filename (csv) of the maze to load.", default="maze_0.csv", type=str)
    args = parser.parse_args()

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
    pygame.display.set_caption(f"BFS Pathfinding on: {args.mazeFile}")
    screen = pygame.display.set_mode(screenSize)


    done = False
    running = False
    closeWindow = False

    # FPS manager
    clock = pygame.time.Clock() 

    # BFS imported from classes.py 
    bfs = BFS(startPosition=startPosition, goalPosition=goalPosition, gridDimension=grid)
   
    # if a key is pressed pygame runs if quit is inputted then the window closes
    while not done:
        for currentEvent in pygame.event.get():
            if currentEvent.type == pygame.KEYDOWN:
                running = True
            elif currentEvent.type == pygame.QUIT:
                done = True
        screen.fill(grey)
        for currentRow in range(numRows):
            for currentColumn in range(numColumns):
                tileColor = colorsList[grid[currentRow, currentColumn]]
                pygame.draw.rect(screen, tileColor,  [width* currentColumn, height * currentRow, width, height])
        
        #change fps to 45
        clock.tick(45)

        pygame.display.flip() # pygame stuff

        if running == True:
            done,solution = bfs.getSuccessors(grid=grid)
            
            frontier = [node.position() for node in bfs.frontier.Queue]
            visited = [node.position() for node in bfs.visited.Queue] 

            for position in frontier:
                    grid[position[0], position[1]] = 6
            for position in visited:
                    grid[position[0], position[1]] = 4
        if done == True:

            for node in solution:
                position = node.position()
                grid[position[0], position[1]] = 5
            screen.fill(grey)
            grid[0, 0] = 2
            grid[-1, -1] = 3

            for currentRow in range(numRows):
                for currentColumn in range(numColumns):
                    tileColor = colorsList[grid[currentRow, currentColumn]]
                    pygame.draw.rect(screen, tileColor,  [width* currentColumn, height * currentRow, width, height])

            #change fps to 45
            clock.tick(45)
            pygame.display.flip() # pygame stuff

    while not closeWindow:
        for currentEvent in pygame.event.get():
            if currentEvent.type == pygame.KEYDOWN:
                closeWindow = True
            elif currentEvent.type == pygame.QUIT:
                closeWindow = True  

    pygame.quit()      