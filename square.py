import pygame
from pygame.locals import *

class Square(pygame.sprite.Sprite):

	squares = pygame.sprite.Group()

	def __init__(self, posx, posy):
		pygame.sprite.Sprite.__init__(self)

		Square.squares.add(self)

		self.image = pygame.Surface([25, 25])
		self.image.fill((255, 0, 0))
		self.rect = self.image.get_rect()
		self.rect.x = posx
		self.rect.y = posy
		self.velx = 0
		self.vely = 0

	def update(self, dt):

		self.rect.x += self.velx
		self.rect.y += self.vely

		if pygame.key.get_pressed()[K_d]:
			self.velx += dt / 10
		else:
			self.velx /= 2

		if pygame.key.get_pressed()[K_a]:
			self.velx -= dt / 10
		else:
			self.velx /= 2

		if pygame.key.get_pressed()[K_w]:
			self.vely += 2 * dt

		if self.rect.y > pygame.display.get_surface().get_height() - 25:
			self.rect.y = pygame.display.get_surface().get_height() - 25
			self.vely *= -0.5

		self.vely += 0.098 * dt
