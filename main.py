
from coordinate import Coordinate
from util import Util
from grid import Grid
from component import Component
import pygame
from random import random
from visualizer import Visualizer

def run():
    util = Util()
  
    gridCellSize = 10
    gridWidth = 500
    gridHeight = 500

    grid = Grid(gridCellSize, gridWidth, gridHeight) 

    component1 = util.constructComponent(20, 20, 100, 200)
    component2 = util.constructComponent(30, 300, 50, 400)
    component3 = util.constructComponent(150, 10, 400, 120)
    component4 = util.constructComponent(200, 300, 250, 400)

    grid.addComponentToStage(component1)
    grid.addComponentToStage(component2)
    grid.addComponentToStage(component3)
    grid.addComponentToStage(component4)

    grid.drawGridLines() 
    grid.naiveFit()
    grid.stayOn()


if  __name__ == '__main__':
    run()

























