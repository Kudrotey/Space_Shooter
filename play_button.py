import pygame.font

class Button:
	
	def __init__(self, ss_game, msg):
		self.screen = ss_game.screen
		self.screen_rect = self.screen.get_rect()

		# Set the dimesions and colour for the button and text
		self.width, self.height = 200,50
		self.button_colour = (0,255,0)
		self.text_colour = (255,255,255)
		self.font = pygame.font.SysFont(None, 48)

		# Create a rect object for the button and center it on the screen
		self.rect = pygame.Rect(0,0,self.width,self.height)
		self.rect.center = self.screen_rect.center

		# Create the text for the button
		self._prep_msg(msg)
		

	def _prep_msg(self, msg):
		'''Turn the text into a rendered image and center it on the button'''
		self.image_msg = self.font.render(msg, True, self.text_colour, self.button_colour)
		self.image_msg_rect = self.image_msg.get_rect()
		self.image_msg_rect.center = self.rect.center


	def draw_msg(self):
		'''Draw the button and then draw on the msg'''
		self.screen.fill(self.button_colour, self.rect) # Drawing the rectangle 
		self.screen.blit(self.image_msg, self.image_msg_rect) # Draw the text image
