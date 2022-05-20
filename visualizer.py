from random import random
import pygame

class Visualizer:

	def __init__(self, width, length):
		pygame.init()
		pygame.display.set_caption('Entity Placement')
		self.screenWidth = width
		self.screenLength = length
		self.surface = pygame.display.set_mode((width,length))
		

	def drawComponent(self, c):
	    color = (random()*1000 % 255,random()*1000 % 255,random()*1000 % 255)
	    some_green = (205, 205, 205)
	    some_green2 = (105, 105, 105)
	    pygame.draw.rect(self.surface, some_green, pygame.Rect(c[0], c[1], c[2], c[3]),  2)
	    pygame.draw.rect(self.surface, some_green2, pygame.Rect(c[0]+2, c[1]+2, c[2]-2, c[3]-2), 0)
	      

	def stayOn(self):
		pygame.display.flip() 
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
