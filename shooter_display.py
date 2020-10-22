import pygame
from pygame.sprite import Sprite 

class ShooterDisplay(Sprite):

	def __init__(self, ss_game):
		super().__init__()
		self.screen = ss_game.screen
		self.settings = ss_game.settings
		self.screen_rect = ss_game.screen.get_rect()

		# Load the image
		self.image = pygame.image.load('shooter.bmp')
		self.image = pygame.transform.rotozoom(self.image, -90, 0.03)
		self.rect = self.image.get_rect()
		self.rect.topright = self.screen_rect.topright