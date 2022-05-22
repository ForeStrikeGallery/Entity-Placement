from util import Util
from visualizer import Visualizer
import time
import copy 

util = Util()

class Grid:
    def __init__(self, cellSize, width, height):
        self.cellSize = cellSize
        self.width = width
        self.height = height
        self.gridComponents = list()
        self.v = Visualizer(width, height)
        self.cMatrix = None

    def takeBackUp(self):
        self.backUpComponents = copy.deepcopy(self.gridComponents)

    def resetFromBackUp(self):
        if not self.backUpComponents:
            raise Exception("No backup taken")

        if len(self.backUpComponents) != len(self.gridComponents):
            raise Exception("Backup size and gridComponents size don't match")

        for i in range(len(self.backUpComponents)):
            self.gridComponents[i].leftDown.x = self.backUpComponents[i].leftDown.x
            self.gridComponents[i].leftDown.y = self.backUpComponents[i].leftDown.y
            self.gridComponents[i].rightUp.x = self.backUpComponents[i].rightUp.x
            self.gridComponents[i].rightUp.y = self.backUpComponents[i].rightUp.y
            self.gridComponents[i].isAnchor = False

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
            self.v.drawComponent(component.getRectParams(self.width, self.height), component.isAnchor)
       
        self.v.displayFlip()
        print("sleeping...")
        time.sleep(0.05)

    def stayOn(self):
        self.v.stayOn()

    def drawGridLines(self):
        self.v.drawGridLines(self.cellSize)

    def naiveFit(self):
        print("Running naiveFit")
        self.takeBackUp()
        attempts = len(self.gridComponents)

        for j in range(attempts):
            print("Attempt: ", j)
            time.sleep(3)
            self.resetFromBackUp()
            anchor = self.gridComponents[j]
            self.gridComponents[j].isAnchor = True

            for i in range(len(self.gridComponents)):
                if i == j:
                    continue

                self.moveCompNearAnchor(self.gridComponents[i], anchor)

    def aboutToOverlapWithOthers(self, comp):

        for c in self.gridComponents:
            if c == comp:
                continue

            if abs(c.leftDown.x - comp.rightUp.x) <= self.cellSize and util.overlapsInY(c, comp):
                return True 

            if abs(c.rightUp.x - comp.leftDown.x) <= self.cellSize and util.overlapsInY(c, comp):
                return True 

            if abs(c.leftDown.y - comp.rightUp.y) <= self.cellSize and util.overlapsInX(c, comp):
                return True 
            
            if abs(c.rightUp.y - comp.leftDown.y) <= self.cellSize and util.overlapsInX(c, comp):
                return True 

        return False


    def moveCompNearAnchor(self, comp, anchor):

        if anchor.rightUp.y < comp.leftDown.y:
            while anchor.rightUp.y + 2 * self.cellSize <= comp.leftDown.y:
               # print(anchor.rightUp.y, comp.leftDown.y)
                if self.aboutToOverlapWithOthers(comp):
                    break

                comp.moveDown(1)
                self.render()

        elif comp.rightUp.y < anchor.rightUp.y:
            while comp.rightUp.y + 2 * self.cellSize <= anchor.leftDown.y:
                if self.aboutToOverlapWithOthers(comp):
                    break
                comp.moveUp(1)
                self.render()

        if anchor.rightUp.x < comp.leftDown.x:
            while anchor.rightUp.x + 2 * self.cellSize <= comp.leftDown.x:
                if self.aboutToOverlapWithOthers(comp):
                    break
                #print(anchor.rightUp.x, comp.leftDown.x)
                comp.moveLeft(1)
                self.render()

        elif comp.rightUp.x < anchor.rightUp.x:
            while comp.rightUp.x + 2 * self.cellSize <= anchor.leftDown.x:
                if self.aboutToOverlapWithOthers(comp):
                    break
                #print(anchor.rightUp.x, comp.leftDown.x)
                comp.moveRight(1)
                self.render()

