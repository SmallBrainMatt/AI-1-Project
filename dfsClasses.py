import time

# doubly ended queue: allows element appending and popping on both sides of the queue
from collections import deque

class Node:
    def __init__(self, position, parentNode):
        self.x = position[0]
        self.y = position[1]
        self.parentNode = parentNode

    def __getitem__(self):
          return (self.x, self.y)

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
    
class DFS:
    def __init__(self, startPosition, goalPosition):
        self.frontier = deque()
        self.visited = set()
        self.startPosition = startPosition
        self.goalPosition = goalPosition