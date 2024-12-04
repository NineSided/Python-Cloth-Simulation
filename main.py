from cloth import *
from vertex import *

import pygame, sys

from pygame.locals import *
pygame.init()


windowsize = [800, 500]
window = pygame.display.set_mode(windowsize)
pygame.display.set_caption("Cloth Simulator")

cloth = Cloth([Vertex()])

while 1:
	window.fill((50, 50, 50))

	cloth.update(window)

	for e in pygame.event.get():
		if e.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
	pygame.time.Clock().tick(60)