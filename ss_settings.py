
class Settings:

	def __init__(self):
		'''Initialise the game static settings'''
		# Screen settings
		self.screen_width = 1000
		self.screen_height = 700
		self.bg_colour = (0,0,0)

		# Shooter settings
		
		self.shooter_limit = 3

		# Laser settings
		self.laser_width = 30
		self.laser_height = 10
		self.laser_colour = (0,230, 75)
		
		self.laser_allowed = 3

		# Spaceship settings
		
		self.spaceship_dropspeed = 3
		

		# How quickly the game speeds up
		self.speedup_scale = 1.1
		self.score_scale = 1.5

		self.initialise_dynamic_settings()

	def initialise_dynamic_settings(self):
		'''Initialise settings that change throughout the game'''
		self.shooter_speed = 0.5
		self.laser_speed = 0.7
		self.spaceship_speed = 0.5

		# -1 represents going up. 1 represents going down
		self.spaceship_direction = -1

		# Scoring
		self.spaceship_points = 50

	def increase_speed(self):
		'''Increase the speed settings'''
		self.shooter_speed *= self.speedup_scale
		self.laser_speed *= self.speedup_scale
		self.spaceship_speed *= self.speedup_scale
		self.spaceship_points = int(self.spaceship_points * self.score_scale)