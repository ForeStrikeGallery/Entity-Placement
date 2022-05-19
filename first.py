

class Component:

    def __init__(self, leftDown, rightUp):
        self.validateCoordinates(leftDown, rightUp)
        self.leftDown = leftDown
        self.rightUp = rightUp

    def validateCoordinates(self, leftDown, rightUp):
        if leftDown.x > rightUp.x or leftDown.y > rightUp.y:
            raise Exception("Coordinates are not set correctly")

class Grid:
    def __init__(self, gridCellSize):
        self.gridCellSize = gridCellSize
        self.gridComponents = list()
   
    def addComponentToStage(self, component):
        # Add component to staging area
        # will arrange in the right place later
        self.gridComponents.append(component) 

    def arrangeComponents(self):
        # Attempt to arrange the components in the grid
        # if successful, return the positions for the comps
        # else, raise and error     
        pass

    def getGridScore(self, connectionMatrix):
        score = 0

        for i in range(len(self.gridComponents)):
            for j in range(len(self.gridComponents)):
                sumConnections = connectionMatrix[i][j] + connectionMatrix[j][i]
                score +=  sumConnections * Util().distBetweenComponents(self.gridComponents[i], self.gridComponents[j])

        return score
        
        

import math

class Util:

    def distBetweenComponents(self, c1, c2):
        x = 0
        y = 0
        if not self.overlapsInX(c1, c2):
            x = min(abs(c1.rightUp.x - c2.leftDown.x), abs(c1.leftDown.x - c2.rightUp.x))

        if not self.overlapsInY(c1, c2):
             y = min(abs(c1.rightUp.y - c2.leftDown.y), abs(c1.leftDown.y - c2.rightUp.y)) 

        return math.sqrt(x*x + y*y)

    def overlapsInX(self, c1, c2):
        return (c2.rightUp.x <= c1.rightUp.x and c2.rightUp.x >= c1.leftDown.x) or (c2.leftDown.x <= c1.rightUp.x and c2.leftDown.x >= c1.leftDown.x)
     
    def overlapsInY(self, c1, c2):
        return (c2.rightUp.y <= c1.rightUp.y and c2.rightUp.y >= c1.leftDown.y) or (c2.leftDown.y <= c1.rightUp.y and c2.leftDown.y >= c1.leftDown.y)
   
class Coordinate:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

def constructComponent(x1, y1, x2, y2):
    leftDown = Coordinate(x1, y1)
    rightUp = Coordinate(x2, y2) 

    return Component(leftDown, rightUp)

def run():
    grid = Grid(1)   

    component1 = constructComponent(1, 2, 3, 4)
    component2 = constructComponent(23, 24, 25, 26)

    grid.addComponentToStage(component1)
    grid.addComponentToStage(component2)
    
    connectionMatrix = [[1, 2], [2, 4]]

    print(grid.getGridScore(connectionMatrix))


if  __name__ == '__main__':
    run()

























