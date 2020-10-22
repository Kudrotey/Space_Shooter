import pygame
from pygame.sprite import Sprite 

class Spaceship(Sprite):
	'''A class that manages the spaceships'''
	def __init__(self, ss_game):
		super().__init__()
		self.screen = ss_game.screen
		self.screen_rect = ss_game.screen.get_rect()
		self.settings = ss_game.settings

		# Load the image and set the position
		self.image = pygame.image.load('spaceship.bmp')
		self.rect = self.image.get_rect()

		self.rect.x = self.screen_rect.width - (2 * self.rect.width)
		self.rect.y = self.rect.height

		self.y = float(self.rect.y)

	def check_edges(self):
		'''Check whether the first row of spaceship has reached the edge'''
		if self.rect.top <= 0 or self.rect.bottom >= self.screen_rect.bottom:
			return True


	def update(self):
		'''Update the postion of the spaceship'''
		self.y += (self.settings.spaceship_speed * 
						self.settings.spaceship_direction)

		self.rect.y = self.y