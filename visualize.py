from random import random
import pygame

class Visualize:

	def __init__(self):
		pygame.init()
		pass 

	def drawComponent(self, screen, c):
	    color = (random()*1000 % 255,random()*1000 % 255,random()*1000 % 255)
	    pygame.draw.rect(screen, color, pygame.Rect(c.leftDown.x, c.leftDown.y, c.rightUp.x, c.rightUp.y),  0)
	    pygame.display.flip()   

	def stayOn(self):
		while True:
			pass 