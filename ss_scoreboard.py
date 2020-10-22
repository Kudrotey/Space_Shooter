import pygame.font
from pygame.sprite import Group


class Scoreboard:
	'''A score to report scoring information'''

	def __init__(self, ss_game):
		'''Initialise the score keeping attributes'''
		self.ss_game = ss_game
		self.screen = ss_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ss_game.settings
		self.stats = ss_game.stats

		# Font settings for scoring information
		self.text_colour = (255,255,255)
		self.font = pygame.font.SysFont(None, 35)
		self.bg_colour = (0,200)

		# Prepare initial score image
		self.prep_score()

	def prep_score(self):
		'''Turn the score into a rendered image'''
		rounded_score = round(self.stats.score, -1)
		score_str = '{:,}'.format(rounded_score)
		self.score_image = self.font.render(score_str, True,
							self.text_colour, self.bg_colour)

		# Display the score at a the lower right
		self.score_rect = self.score_image.get_rect()
		self.score_rect.bottomright = self.screen_rect.bottomright


	def show_score(self):
		'''Draw the score on the screen'''
		self.screen.blit(self.score_image, self.score_rect)
