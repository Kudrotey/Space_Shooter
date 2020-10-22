import pygame


class Shooter:

	def __init__(self, ss_game):
		# Set up the screen 
		
		self.screen = ss_game.screen
		self.settings = ss_game.settings
		self.screen_rect = ss_game.screen.get_rect()

		# Load the image
		self.image = pygame.image.load('shooter.bmp')
		self.image = pygame.transform.rotozoom(self.image, -90, 0.1)
		self.rect = self.image.get_rect()

		# Position image
		self.rect.midleft = self.screen_rect.midleft

		# Give float value to the speed of shooter
		self.y = float(self.rect.y)

		# Setting up a flag for movement of shooter
		self.moving_up = False
		self.moving_down = False

	def update(self):
		'''Updating the position of the shooter'''
		if self.moving_up and self.rect.top > self.screen_rect.top:
			self.y -= self.settings.shooter_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.shooter_speed
		# Update the rect object from self.y
		self.rect.y = self.y

	def center_shooter(self):
		'''Position the shooter on the center'''
		self.rect.midleft = self.screen_rect.midleft
		self.y = float(self.rect.y)

	def blitme(self):
		# Draw the ship at its current location
		self.screen.blit(self.image, self.rect)


