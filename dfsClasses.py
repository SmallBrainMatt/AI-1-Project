import time

class Node:
    def __init__(self, position, parentNode):
        self.x = position[0]
        self.y = position[1]
        self.parentNode = parentNode

  #  def __getitem__(self):
  #        return (self.x, self.y)

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
        self.frontier = []
        self.visited = set()
        self.startPosition = startPosition
        self.goalPosition = goalPosition
        
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
        currentNode = self.frontier.pop() # popping right for last in first out method
        x, y = currentNode.position()

        right=(1,0)
        left=(-1,0)
        up=(0,1)
        down=(0, -1)

        # first movements expanded are down, right, up , then left because of the stack
        possibleMovements = [down,left,right,up]

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
                    return done, solution, endTime   
                   
        # goaL not found, add node to visited and move  to next node
        self.visited.add(currentNode.position())
        done = False
        solution = []
        return done, [], 0