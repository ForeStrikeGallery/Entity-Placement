from random import random
import pygame

class Visualizer:

	def __init__(self, width, length):
		pygame.init()
		pygame.display.set_caption('Entity Placement')
		self.screenWidth = width
		self.screenLength = length
		self.surface = pygame.display.set_mode((width,length))
		

	def drawComponent(self, c, isAnchor):
	    random_color = (random()*1000 % 255,random()*1000 % 255,random()*1000 % 255)
	    dark_grey = (205, 205, 205)
	    light_grey = (105, 105, 105)
	    anchor_color = (10, 10, 10)

	    if not isAnchor:
		    pygame.draw.rect(self.surface, dark_grey, pygame.Rect(c[0], c[1], c[2], c[3]),  2)
		    pygame.draw.rect(self.surface, light_grey, pygame.Rect(c[0]+2, c[1]+2, c[2]-2, c[3]-2), 0)
	    else:
	    	pygame.draw.rect(self.surface, dark_grey, pygame.Rect(c[0], c[1], c[2], c[3]),  2)
	    	pygame.draw.rect(self.surface, anchor_color, pygame.Rect(c[0]+2, c[1]+2, c[2]-2, c[3]-2), 0)
	      
  	def displayFlip(self):
  		pygame.display.flip() 

	def stayOn(self):
		while True:
			pass 

	def drawGridLines(self, gridCellSize):
		red = (40,0,0)
		x = 10
		while x < self.screenWidth:
			pygame.draw.line(self.surface, red, pygame.Vector2(x, 0), pygame.Vector2(x, self.screenLength))
			x += 10

		y = 10
		while y < self.screenLength:
			pygame.draw.line(self.surface, red, pygame.Vector2(0, y), pygame.Vector2(self.screenWidth, y))
			y += 10

	def clearScreen(self):
		self.surface.fill((0,0,0))
