
from coordinate import Coordinate
from util import Util
from grid import Grid
from component import Component
import pygame
from random import random
from visualize import Visualize

def run():
    util = Util()
    grid = Grid(1) 
    v = Visualize()  

    component1 = util.constructComponent(3, 3, 50, 60)
    component2 = util.constructComponent(10, 15, 25, 35)

    grid.addComponentToStage(component1)
    grid.addComponentToStage(component2)
    
    connectionMatrix = [[1, 2], [2, 4]]

    pygame.init()

    surface = pygame.display.set_mode((400,300))
    
    v.drawComponent(surface, component1)
    v.drawComponent(surface, component2)

    print(grid.getGridScore(connectionMatrix))

    v.stayOn()

    

if  __name__ == '__main__':
    run()

























