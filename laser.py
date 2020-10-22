import pygame
from pygame.sprite import Sprite

class Laser(Sprite):

	def __init__(self, ss_game):
		'''Create a laser pointer at the shooters location'''
		super().__init__()
		self.screen = ss_game.screen
		self.settings = ss_game.settings
		self.colour = self.settings.laser_colour

		# Create a laser at rect (0,0) and then position it on the shooter
		self.rect = pygame.Rect(0,0, 
								self.settings.laser_width,
								self.settings.laser_height)
		self.rect.midright = ss_game.shooter.rect.midright

		self.x = float(self.rect.x)

	def update(self):
		'''Update the laser when shootind off from the shooter'''
		self.x += self.settings.laser_speed
		# Update the rect position
		self.rect.x = self.x

	def draw_laser(self):
		# Draw the laser onto the screen
		pygame.draw.rect(self.screen, self.colour, self.rect)