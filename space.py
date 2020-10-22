import pygame

class Space:

	def __init__(self, ss_game):
		self.screen = ss_game.screen
		self.settings = ss_game.settings
		self.screen_rect = self.screen.get_rect()

		self.image = pygame.image.load('space_bg.bmp')
		self.image = pygame.transform.scale(self.image, (self.settings.screen_width,
															self.settings.screen_height))

		self.image_rect = self.image.get_rect()
		self.image_rect.center = self.screen_rect.center

	def blitme(self):
		self.screen.blit(self.image, self.image_rect)

