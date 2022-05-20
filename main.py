
from coordinate import Coordinate
from util import Util
from grid import Grid
from component import Component
import pygame
from random import random
from visualizer import Visualizer

def run():
    util = Util()
    grid = Grid(1, 300, 400) 
    # v = Visualizer(300, 400)  

    pygame.init()

    component1 = util.constructComponent(3, 3, 50, 60)
    component2 = util.constructComponent(10, 15, 25, 35)
    component3 = util.constructComponent(40, 100, 110, 115)
    component4 = util.constructComponent(100, 12, 110, 35)

    grid.addComponentToStage(component1)
    grid.addComponentToStage(component2)
    grid.addComponentToStage(component3)
    grid.addComponentToStage(component4)
    
    connectionMatrix = [[1, 2, 1, 3], [1, 2, 1, 3], [1, 2, 1, 3], [1, 2, 1, 3]]

    grid.display()
    
    # v.drawComponent(component1)
    # v.drawComponent(component2)
    # v.drawComponent(component3)
    # v.drawComponent(component4)

    print(grid.getGridScore(connectionMatrix))

    # v.stayOn()

    

if  __name__ == '__main__':
    run()

























