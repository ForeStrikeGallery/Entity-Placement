from coordinate import Coordinate
from component import Component
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

    def constructComponent(self, leftUpX, leftUpY, rightUpX, rightUpY):
        leftDown = Coordinate(leftUpX, leftUpY)
        rightUp = Coordinate(rightUpX, rightUpY)

        return Component(leftDown, rightUp)