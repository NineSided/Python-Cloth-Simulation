from cloth import *
from vertex import *

import pygame, sys

from pygame.locals import *
pygame.init()

windowsize = [800, 500]
surface = pygame.display.set_mode(windowsize)
pygame.display.set_caption("Cloth Simulator")

window = pygame.Surface(windowsize)

cloth = Cloth([Vertex(anchored=True)])

newvert = Vertex(origin=(200, 100))
cloth.verticies[0].connectives.append(newvert)
cloth.verticies.append(newvert)

while 1:
	window.fill((50, 50, 50))

	cloth.update(window)

	if pygame.mouse.get_pressed()[0]:
		cloth.verticies[len(cloth.verticies)-1].rect.x = pygame.mouse.get_pos()[0]
		cloth.verticies[len(cloth.verticies)-1].rect.y = pygame.mouse.get_pos()[1]

	for e in pygame.event.get():
		if e.type == QUIT:
			pygame.quit()
			sys.exit()
			
	surface.blit(pygame.transform.scale(window, windowsize), (0, 0))

	pygame.display.update()
	pygame.time.Clock().tick(60)