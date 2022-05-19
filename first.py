
from coordinate import Coordinate
from util import Util
from grid import Grid
from component import Component

# , Util, Component, Grid

def constructComponent(x1, y1, x2, y2):
    leftDown = Coordinate(x1, y1)
    rightUp = Coordinate(x2, y2) 

    return Component(leftDown, rightUp)

def run():
    util = Util()
    grid = Grid(1)   

    component1 = util.constructComponent(1, 2, 3, 4)
    component2 = util.constructComponent(23, 24, 25, 26)

    grid.addComponentToStage(component1)
    grid.addComponentToStage(component2)
    
    connectionMatrix = [[1, 2], [2, 4]]

    print(grid.getGridScore(connectionMatrix))


if  __name__ == '__main__':
    run()

























