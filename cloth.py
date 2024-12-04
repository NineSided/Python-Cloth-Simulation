import pygame

class Cloth:
	def __init__(self, verticies):
		self.verticies = verticies

	def update(self, surface):
		#for vert in self.verticies:
		#	vert.update()

		self.show(surface)

	def show(self, surface):
		for vert in self.verticies:
			pygame.draw.circle(surface, vert.color, (vert.rect.x, vert.rect.y), vert.size)