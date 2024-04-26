from collections import deque



class Node:
    def __init__(self, position, parentNode):
        self.x = position[0]
        self.y = position[1]
        self.parentNode = parentNode

    def __getitem__(self):
          return (self.x, self.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

    def position(self):
        return (self.x, self.y)
    


# checks if the position passed in is a valid move or not
def isValidMove(position):
    (x,y) = position
    xValid = (x<=40) & (x>=0) # if x is is within grid dimensions and that it does not go backwards
    yValid = (y<=40) & (y>=0) # if y is is within grid dimensions and that it does not go backwards
    if (xValid and yValid): 
        return True
    else: 
        return False

class wallfollowing:
    def __init__(self, startPosition, goalPosition):
        self.startPosition = startPosition
        self.goalPosition = goalPosition

    def get_path(self, maze):
        start_x, start_y = self.startPosition
        goal_x, goal_y = self.goalPosition

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        direction = 0  # Initial direction: right

        x, y = start_x, start_y
        path = [(x, y)]

        while (x, y) != (goal_x, goal_y):
            # Look to the right
            right_dir = directions[(direction - 1) % 4]
            right_x, right_y = x + right_dir[0], y + right_dir[1]

            # Go forward
            dx, dy = directions[direction]
            new_x, new_y = x + dx, y + dy

            if maze[new_x][new_y] == 0:  # Move forward
                x, y = new_x, new_y
                path.append((x, y))
            elif maze[right_x][right_y] == 0:  # Turn right
                direction = (direction - 1) % 4
                path.append((x, y))
            elif maze[new_x][new_y] != 1:  # If the left is not a wall, turn left
                direction = (direction + 1) % 4
                x, y = new_x, new_y
                path.append((x, y))
            else:  # If the left is a wall, turn around
                direction = (direction + 2) % 4

        return path

