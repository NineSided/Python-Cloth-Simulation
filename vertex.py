import pygame

class Vertex:
	def __init__(self, origin=(0, 0) color=(100, 100, 100), size=5):
		self.color = color
		self.size = size
		self.connectives = []

		self.movement = pygame.math.Vector2(0, 0)
		self.rect = pygame.Rect(self.origin[0], self.origin[1], size, size)

	def update(self):
		for c in self.connectives:
			dx, dy = self.rect