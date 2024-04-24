class Node:
    def __init__(self, position, parentNode):
        self.x = position[0]
        self.y = position[1]
        self.parentNode = parentNode

    def __getitem__(self):
          return (self.x, self.y)

    def position(self):
        return (self.x, self.y)
    
class Queue:
    def __init__(self):
        self.Queue = []

    def __len__(self):
        return len(Queue)

    def append(self, node):
        self.Queue.append(node)

    def getNode(self):
        return self.Queue[0]

    def remove(self):
        self.Queue = self.Queue[1:len(self.Queue)]


# checks if the position passed in is a valid move or not
def isValidMove(position, gridDimension):
    (x,y) = position
    xValid = (x<=40) & (x>=0) # if x is is within grid dimensions and that it does not go backwards
    yValid = (y<=40) & (y>=0) # if y is is within grid dimensions and that it does not go backwards
    if (xValid and yValid): 
        return True
    else: 
        return False



class BFS:
    def __init__(self, startPosition, goalPosition, gridDimension):
        self.explored = Queue()
        self.frontier = Queue()

        # Root node initialized and added to frontier
        node = Node(position=startPosition, parentNode=None)
        self.frontier.append(node)

        self.gridDimension = gridDimension
        self.startPosition = startPosition
        self.goalPosition = goalPosition
    
    # method that is ran only when the currentNode is the goal node
    def getSolutionPath(self, currentNode):
        solutionPath=[]
        while currentNode.parent != None:
            solutionPath.append(currentNode)
    
    def getSuccessors(self, grid):
        currentNode = self.frontier.getNode()
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
                    done = True
                    solution = self.getSolutionPath(currentNode=newNode)
                    self.explored.append(self.frontier.getNode())
                    self.frontier.remove()
                    return solution,done
        
        # goaL not found, add node to explored and move  to next node
        self.explored.Queue.append(currentNode)
        self.frontier.remove()
        done = False
        NoSolution = []
        return NoSolution, done
