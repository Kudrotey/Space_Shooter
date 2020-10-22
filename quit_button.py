import pygame.font

class QuitButton:

	def __init__(self, ss_game, msg):
		self.screen = ss_game.screen
		self.screen_rect = self.screen.get_rect()

		# Set the dimension of the buttons and settings for text
		self.width, self.height = 200, 50
		self.button_colour = (0,255,0)
		self.text_colour = (255,255,255)
		self.font = pygame.font.SysFont(None, 48)

		# Create a rect of the button and set its position
		self.rect = pygame.Rect(0,0,self.width, self.height)
		self.rect.x = self.rect.left + (self.screen_rect.width)/2 - (self.rect.width)/2
		self.rect.y = (self.screen_rect.height)/2 + self.rect.height

		# Create the text for the button
		self._prep_quit(msg)

	def _prep_quit(self, msg):
		'''Turn the text into a rendered image'''
		self.image_quit = self.font.render(msg, True, 
							self.text_colour, self.button_colour)
		self.image_quit_rect = self.image_quit.get_rect()
		self.image_quit_rect.center = self.rect.center

	def draw_msg(self):
		self.screen.fill(self.button_colour, self.rect)
		self.screen.blit(self.image_quit, self.image_quit_rect)