import sys
from time import sleep

import pygame

from ss_settings import Settings
from shooter import Shooter
from space import Space 
from laser import Laser
from spaceship import Spaceship 
from main_stats import Stats
from play_button import Button 
from quit_button import QuitButton 
from ss_scoreboard import Scoreboard 
from shooter_display import ShooterDisplay

class SpaceShooter:
	'''The main class that controls all assets and behaviour of the game'''

	def __init__(self):
		# Setting up the screen 
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption('SpaceShooter')

		self.stats = Stats(self)
		self.space_bg = Space(self)
		self.shooter = Shooter(self)
		# Create a list that will store the lasers
		self.lasers = pygame.sprite.Group()
		self.spaceships = pygame.sprite.Group()
		self.display_shooters = pygame.sprite.Group()

		self._create_fleet()
		self._display_shooters()

		self.button = Button(self,'Play')
		self.quitbutton = QuitButton(self, 'Quit')

		self.sb = Scoreboard(self)

	def run_game(self):

		while True:
			self._check_events()

			if self.stats.game_active:
			
				self.shooter.update()
				self._update_lasers()
				self._update_spaceships()

			self._screen_updates()



	def _check_events(self):
		# Pressing certain key types
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					self.shooter.moving_up = True
				if event.key == pygame.K_DOWN:
					self.shooter.moving_down = True
				if event.key == pygame.K_q:
					sys.exit()
				if event.key == pygame.K_SPACE:
					self._fire_laser()

			elif event.type == pygame.KEYUP:
				self.shooter.moving_up = False
				self.shooter.moving_down = False

			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)
				self._check_quit_button(mouse_pos)
	
	def _check_play_button(self, mouse_pos):
		'''Start a new game when the player clicks play'''
		button_clicked = self.button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:
			# Reset the game settings
			self.settings.initialise_dynamic_settings()
			# Reset the whole game so it starts from the beginning
			self.stats.reset_stats()
			self._display_shooters()
			self.stats.game_active = True
			self.sb.prep_score()

			self.spaceships.empty()
			self.lasers.empty()

			self._create_fleet()
			self.shooter.center_shooter()

			# Hide the mouse cursor
			pygame.mouse.set_visible(False)

	def _check_quit_button(self, mouse_pos):
		'''Quit the quit when the quit button is clicked'''
		quit_button_clicked = self.quitbutton.rect.collidepoint(mouse_pos)
		if quit_button_clicked and not self.stats.game_active and self.stats.shooter_left == 0:
			sys.exit()

	def _fire_laser(self):
		'''Create a new laser and add it to the group'''
		if len(self.lasers) < self.settings.laser_allowed:
			new_laser = Laser(self)
			self.lasers.add(new_laser)

	def _update_lasers(self):
		self.lasers.update()

		# Get rid of bullets that have disappeared
		for laser in self.lasers.copy():
			if laser.rect.left >= self.settings.screen_width:
				self.lasers.remove(laser)

		self._check_lasers_spaceships_collisions()

	def _check_lasers_spaceships_collisions(self):
		'''Respond to laser spaceship collisions'''
		#Check for collisions between lasers and spaceship
		# Destroy the spaceship
		collisions = pygame.sprite.groupcollide(
				self.lasers, self.spaceships, False, True)

		if collisions:
			for spaceships in collisions.values():
				self.stats.score += self.settings.spaceship_points * len(spaceships)
			self.sb.prep_score()

		# Add a new fleet of spaceships when they dissapear
		if not self.spaceships:
			self.lasers.empty()
			self._create_fleet()
			self.settings.increase_speed()

	def _create_fleet(self):
		'''Create a fleet of spaceship'''
		spaceship = Spaceship(self)
		spaceship_height, spaceship_width = spaceship.rect.size 
		# Number of spaceships that fit on the screen vertically
		shooter_width = self.shooter.rect.width
		available_space_y = self.settings.screen_height - (2 * spaceship_height)
		number_spaceship_y = available_space_y // (1 * spaceship_height)

		# Number of spaceships that fit on the screen horizontally 
		available_space_x = (self.settings.screen_width - 
								(3 * spaceship_width) - (shooter_width))
		number_columns = available_space_x // (3 * spaceship_width)

		for number_column in range(number_columns):
			for number_spaceship in range(number_spaceship_y):
				self._create_spaceship(number_spaceship, number_column)

	def _create_spaceship(self, number_spaceship, number_column):
		# Creatings spaceship and setting the position
		spaceship = Spaceship(self)
		spaceship_width, spaceship_height = spaceship.rect.size

		spaceship.y = spaceship_height + (2 * spaceship_height * number_spaceship)
		spaceship.rect.y = spaceship.y 

		spaceship.x = (self.settings.screen_width - 
						(2 * spaceship_width + (2 * spaceship_width * number_column)))
		spaceship.rect.x = spaceship.x

		self.spaceships.add(spaceship)

	def _display_shooters(self):
		display_shooter = ShooterDisplay(self)
		display_shooter_width = display_shooter.rect.width
		
		for shooter_number in range(self.stats.shooter_left):
			display_shooter = ShooterDisplay(self)
			display_shooter.rect.x = self.settings.screen_width - (display_shooter_width * shooter_number) - display_shooter_width
			display_shooter.rect.y = display_shooter.rect.height / 2
			self.display_shooters.add(display_shooter)

	def _remove_display_shooters(self):

		for display_shooter in self.display_shooters.copy():
				if len(self.display_shooters) > self.stats.shooter_left:
					self.display_shooters.remove(display_shooter)

	def _update_spaceships(self):
		'''Update the position of the fleet of spaceships'''
		self._check_fleet_edges()
		self.spaceships.update()

		# Collision between the shooter and spaceships
		if pygame.sprite.spritecollideany(self.shooter, self.spaceships):
			self._shooter_hit() 

		self._check_spaceships_bottom()

	def _check_fleet_edges(self):
		'''Respond appropriately when spaceship reaches the edges'''
		for spaceship in self.spaceships.sprites():
			if spaceship.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		'''Move the fleet left and then move it down'''
		for spaceship in self.spaceships.sprites():
			spaceship.rect.x -= self.settings.spaceship_dropspeed
		self.settings.spaceship_direction *= -1

	def _screen_updates(self):
		# Updating the screen
		self.space_bg.blitme()
		self.shooter.blitme()

		for laser in self.lasers.sprites():
			laser.draw_laser()

		self.spaceships.draw(self.screen)
		self.display_shooters.draw(self.screen)
		
		self.sb.show_score()
		
		if not self.stats.game_active:
			self.button.draw_msg()
			if self.stats.shooter_left == 0:
				self.quitbutton.draw_msg()

		pygame.display.flip()

	def _shooter_hit(self):
		'''Respond to the shooter being hit by a spaceship'''

		if self.stats.shooter_left > 0:
			# Decrement shooter left
			self.stats.shooter_left -= 1
			# Get rid of any remaining lasers and spaceships
			self._remove_display_shooters()
			
			self.spaceships.empty()
			self.lasers.empty()

			# Create a new fleet and center the shooter
			self._create_fleet()
			self.shooter.center_shooter()

			# Pause the game to see the collision
			sleep(0.5)


		else:
			self.stats.game_active = False
			
			pygame.mouse.set_visible(True)

	def _check_spaceships_bottom(self):
		'''Check to see if the spaceships have reached 
		   the left side of the screen'''

		screen_rect = self.screen.get_rect()
		for spaceship in self.spaceships.sprites():
			if spaceship.rect.left <= screen_rect.left:
				self._shooter_hit()
				break

if __name__ == '__main__':
	ss = SpaceShooter()
	ss.run_game()
