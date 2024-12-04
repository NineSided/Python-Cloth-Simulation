import pygame, sys

from pygame.locals import *
pygame.init()


windowsize = [800, 500]
window = pygame.display.set_mode(windowsize)

while 1:
	window.fill((50, 50, 50))

	for e in pygame.event.get():
		if e.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
	pygame.time.Clock().tick(60)