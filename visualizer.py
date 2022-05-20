from random import random
import pygame

class Visualizer:

	def __init__(self, width, length):
		pygame.init()
		pygame.display.set_caption('Entity Placement')
		self.surface = pygame.display.set_mode((width,length))
		

	def drawComponent(self, c):
	    color = (random()*1000 % 255,random()*1000 % 255,random()*1000 % 255)
	    pygame.draw.rect(self.surface, color, pygame.Rect(c[0], c[1], c[2], c[3]),  0)
	      

	def stayOn(self):
		pygame.display.flip() 
		while True:
			pass 