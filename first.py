

class Component:

    def __init__(self, leftDown, rightUp):
        self.validateConfigs(leftDown, rightUp)
        self.leftDown = leftDown
        self.rightUp = rightUp

    def validateCoordinates(leftDown, rightUp):
        if leftDown.x > rightUp.x or lefDown.y > rightUp.y:
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
                score += (connectionMatrix[i][j] + connectionMatrix[j][i]) * Util.distBetweenComponents(self.gridComponents[i], self.gridComponents[j])


        return score
        
        

class Util:

    def distBetweenComponents(c1, c2):
        x = 0
        y = 0
        if not self.overlapsInX(c1, c2):
            x = min(abs(c1.righUpper.x - c2.lefDown.x), abs(c1.lefDown.x - c2.righUpper.x))

        if not self.overlapsInY(c1, c2):
             y = min(abs(c1.righUpper.y - c2.lefDown.y), abs(c1.lefDown.y - c2.righUpper.y)) 

        return (x, y)

    def overlapsInX(c1, c2):
        return c1.righUpper.x > c2.lefDown.x or c2.righUpper.x > c1.lefDown.x
     
    def overlapsInY(c1, c2):
        return c1.righUpper.y > c2.lefDown.y or c2.righUpper.y > c1.lefDown.y
   
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
    component2 = constructComponent(2, 3, 4, 5)

    grid.addComponentToStage(component1)
    grid.addComponentToStage(component2)
    
    connectionMatrix = [[1, 2], [2, 4]]

    print(getGridScore(connectionMatrix))


if  __name__ == '__main__':
    run()

























