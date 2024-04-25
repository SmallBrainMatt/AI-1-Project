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



class BFS:
    def __init__(self, startPosition, goalPosition):
        self.frontier = deque() # doubly ended queue
        self.visited = set()

        # Root node initialized and added to frontier
        node = Node(position=startPosition, parentNode=None)
        self.frontier.append(node)

        #self.gridDimension = gridDimension
        self.startPosition = startPosition
        self.goalPosition = goalPosition
    
    # method that is ran only when the currentNode is the goal node
    def getSolutionPath(self, currentNode):
        solutionPath=[]
        while currentNode.parentNode != None:
            solutionPath.append(currentNode)
            currentNode = currentNode.parentNode
        return solutionPath
    
    def getSuccessors(self, grid):
        # if there are no more nodes in the frontier then there is no solution, animation will represent that.
        if not self.frontier:
                return False, [], 0 
        currentNode = self.frontier.popleft()
        x, y = currentNode.position()

        right=(1,0)
        left=(-1,0)
        up=(0,1)
        down=(0, -1)

        possibleMovements = [right,left,up,down]

        for movement in possibleMovements:
            # Sets moveX and moveY to each possible movement
            moveX, moveY = movement
            positionToCheck = (x+moveX, y+moveY)
            if (isValidMove(positionToCheck) and (grid[positionToCheck[0], positionToCheck[1]] in [1,3]) ):
                newNode = Node(parentNode=currentNode, position=positionToCheck)
                self.frontier.append(newNode)
                if newNode.position() == self.goalPosition: # then that is the goal node and the solution path is returned
                    endTime = time.time()
                    done = True
                    solution = self.getSolutionPath(currentNode=newNode)
                    #self.visited.append(self.frontier.getNode())
                    #self.frontier.remove()
                    return done, solution, endTime
        
        # goaL not found, add node to visited and move  to next node
        #self.visited.Queue.append(currentNode)
        #self.frontier.remove()
        self.visited.add(currentNode.position())
        done = False
        solution = []
        return done, [], 0
