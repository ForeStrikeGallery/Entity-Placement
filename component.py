cellSize = 10

class Component:

    def __init__(self, leftDown, rightUp):
        self.validateCoordinates(leftDown, rightUp)
        self.leftDown = leftDown
        self.rightUp = rightUp
        self.isAnchor = False

    def validateCoordinates(self, leftDown, rightUp):
        if leftDown.x > rightUp.x or leftDown.y > rightUp.y:
            raise Exception("Coordinates are not set correctly")

    def getRectParams(self, gridWidth, gridHeight):
        return (self.leftDown.x, gridHeight - self.rightUp.y, self.rightUp.x - self.leftDown.x, self.rightUp.y - self.leftDown.y)

    def moveUp(self, blocks):
        self.rightUp.y += blocks * cellSize
        self.leftDown.y += blocks * cellSize


    def moveDown(self, blocks):
        self.rightUp.y -= blocks * cellSize
        self.leftDown.y -= blocks * cellSize


    def moveLeft(self, blocks):
        self.rightUp.x -= blocks * cellSize
        self.leftDown.x -= blocks * cellSize

    def moveRight(self, blocks):
        self.rightUp.x += blocks * cellSize
        self.leftDown.x += blocks * cellSize

    

