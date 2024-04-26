import argparse
import pygame
import numpy as np
from wfollowingClasses import wallfollowing

black = (0, 0, 0)          # Black
white = (255, 255, 255)    # White
green = (0, 255, 0)        # Green
red = (255, 0, 0)          # Red
yellow = (255, 255, 0)     # Yellow

def draw_maze(screen, maze, width, height):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            color = white if maze[row][col] == 1 else black
            pygame.draw.rect(screen, color, [col * width, row * height, width, height])

def draw_path(screen, path, width, height):
    for x, y in path:
        pygame.draw.rect(screen, red, [y * width, x * height, width, height])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mazeFile", help="filename (csv) of the maze to load.", default="maze_0.csv", type=str)
    args = parser.parse_args()

    maze_address = "mazes/" + args.mazeFile
    maze = np.genfromtxt(maze_address, delimiter=',').astype(int)

    # Define start and goal positions
    start_position = (0, 0)
    goal_position = (maze.shape[0] - 1, maze.shape[1] - 1)

    # Create an instance of wallfollowing class with start and goal positions
    wf = wallfollowing(start_position, goal_position)

    # Get path using wall following
    path = wf.get_path(maze)

    # Pygame setup
    width = height = 20
    screen_size = (maze.shape[1] * width, maze.shape[0] * height)

    pygame.init()
    pygame.display.set_caption(f"Wall Following on: {args.mazeFile}")
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(white)
        draw_maze(screen, maze, width, height)
        draw_path(screen, path, width, height)

        pygame.display.flip()
        clock.tick(5)  # Adjust the frame rate

    pygame.quit()

if __name__ == "__main__":
    main()





