from util import Util

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
        