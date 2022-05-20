from util import Util
from visualizer import Visualizer
import time

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

    def render(self):
        self.v.clearScreen()
        self.drawGridLines()
        
        for component in self.gridComponents:
            self.v.drawComponent(component.getRectParams(self.width, self.height))
       
        self.v.displayFlip()
        print("sleeping...")
        time.sleep(0.05)

    def stayOn(self):
        self.v.stayOn()

    def drawGridLines(self):
        self.v.drawGridLines(self.cellSize)

    def naiveFit(self):
        print("Running naiveFit")
        anchor = self.gridComponents[0]

        for i in range(len(self.gridComponents)):
            if i == 0:
                continue

            self.moveCompNearCenterComp(self.gridComponents[i], anchor)

    def moveCompNearCenterComp(self, comp, anchor):

        if anchor.rightUp.y < comp.leftDown.y:
            while anchor.rightUp.y + 2 * self.cellSize <= comp.leftDown.y:
                print(anchor.rightUp.y, comp.leftDown.y)
                comp.moveDown(1)
                self.render()

            # move comp down until it hits
        elif comp.rightUp.y < anchor.rightUp.y:
            # move comp up until it hits
            while comp.rightUp.y + 2 * self.cellSize <= anchor.leftDown.y:
                comp.moveUp(1)
                self.render()

        if anchor.rightUp.x < comp.leftDown.x:
            while anchor.rightUp.x + 2 * self.cellSize <= comp.leftDown.x:
                print(anchor.rightUp.x, comp.leftDown.x)
                comp.moveLeft(1)
                self.render()
            # move comp right  until it hits
        elif comp.rightUp.x < anchor.rightUp.x:
            while comp.rightUp.x + 2 * self.cellSize <= anchor.leftDown.x:
                print(anchor.rightUp.x, comp.leftDown.x)
                comp.moveRight(1)
                self.render()
            # move comp up until it hits

