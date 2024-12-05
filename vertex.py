import pygame, math

class Vertex:
	def __init__(self, origin=(100, 100), color=(100, 100, 100), size=5, anchored=False):
		self.color = color
		self.size = size
		self.connectives = []
		
		self.anchored = anchored
		self.yvel = 0

		self.movements = []
		self.movement = pygame.math.Vector2(0, 0)
		self.rect = pygame.Rect(origin[0], origin[1], size, size)

	def update(self):
		for c in self.connectives:
			dx, dy = self.rect.x-c.rect.x, self.rect.y-c.rect.y
			angle = math.atan2(dy, dx)
			mx, my = math.cos(angle), math.sin(angle)

			m = (mx, my)
			c.movements.append(m)

		for c in self.connectives:
			distance = math.dist((self.rect.x, self.rect.y), (c.rect.x, c.rect.y))
			dist = distance*0.1

		#if self.anchored == False:
		#	self.yvel += 0.2
		#	if self.yvel > 3:
		#		self.yvel = 3
		#	self.movements.append((0, self.yvel))
			
		for m in self.movements:
			self.movement.x += m[0]
			self.movement.y += m[1]
			self.movements.remove(m)

		self.rect.x += self.movement.x
		self.rect.y += self.movement.y