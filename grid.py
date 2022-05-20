from util import Util
from visualizer import Visualizer

class Grid:
    def __init__(self, cellSize, width, height):
        self.cellSize = cellSize
        self.width = width
        self.height = height
        self.gridComponents = list()
        self.v = Visualizer(width, height)
        self.cMatrix = None

    def addComponentToStage(self, component):
        # Add component to staging area
        # will arrange in the right place later
        self.gridComponents.append(component) 

    def arrangeComponents(self):
        # Attempt to arrange the components in the grid
        # if successful, return the positions for the comps
        # else, raise and error     
        pass

    def setConnectionMatrix(self, cMatrix):
        self.cMatrix = cMatrix

    def getGridScore(self):

        if self.cMatrix == None:
            raise Exception("Connection matrix not set")

        score = 0

        for i in range(len(self.gridComponents)):
            for j in range(len(self.gridComponents)):
                sumConnections = self.cMatrix[i][j] + self.cMatrix[j][i]
                score +=  sumConnections * Util().distBetweenComponents(self.gridComponents[i], self.gridComponents[j])

        return score

    def display(self):
        for component in self.gridComponents:
            self.v.drawComponent(component)
        self.v.stayOn()