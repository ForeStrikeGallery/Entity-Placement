
from coordinate import Coordinate
from util import Util
from grid import Grid
from component import Component
import pygame
from random import random

# , Util, Component, Grid

def constructComponent(x1, y1, x2, y2):
    leftDown = Coordinate(x1, y1)
    rightUp = Coordinate(x2, y2) 

    return Component(leftDown, rightUp)


def drawComponent(screen, c):
    color = (random()*1000 % 255,random()*1000 % 255,random()*1000 % 255)
    pygame.draw.rect(screen, color, pygame.Rect(c.leftDown.x, c.leftDown.y, c.rightUp.x, c.rightUp.y),  0)
    pygame.display.flip()    
   

def run():
    util = Util()
    grid = Grid(1)   

    component1 = util.constructComponent(30, 40, 50, 60)
    component2 = util.constructComponent(10, 15, 25, 35)

    grid.addComponentToStage(component1)
    grid.addComponentToStage(component2)
    
    connectionMatrix = [[1, 2], [2, 4]]

    pygame.init()

    surface = pygame.display.set_mode((400,300))
    
    drawComponent(surface, component1)
    drawComponent(surface, component2)

    print(grid.getGridScore(connectionMatrix))

    while True:
        pass 

    

if  __name__ == '__main__':
    run()

























