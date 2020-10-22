
class Stats:
	'''Class that manages stats for the game'''

	def __init__(self, ai_game):
		'''Initialize the stats'''
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.reset_stats()
		

		# Start SpaceShooter in an active state
		self.game_active = False

	def reset_stats(self):
		self.shooter_left = self.settings.shooter_limit
		self.score = 0