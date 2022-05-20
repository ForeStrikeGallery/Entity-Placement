
from coordinate import Coordinate
from util import Util
from grid import Grid
from component import Component
import pygame
from random import random
from visualizer import Visualizer

def run():
    util = Util()

    gridCellSize = 1
    gridWidth = 500
    gridHeight = 400

    grid = Grid(gridCellSize, gridWidth, gridHeight) 

    component1 = util.constructComponent(20, 20, 100, 200)
    component2 = util.constructComponent(10, 15, 25, 35)
    component3 = util.constructComponent(40, 100, 110, 115)
    component4 = util.constructComponent(100, 12, 110, 35)

    grid.addComponentToStage(component1)
    grid.addComponentToStage(component2)
    grid.addComponentToStage(component3)
    grid.addComponentToStage(component4)
    
    grid.display()


if  __name__ == '__main__':
    run()

























