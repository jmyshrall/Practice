"""
File: alien.py
Collaborator: Justin Myshrall
Created: 9/7/2023
"""

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """
	A class used to represent an alien
	"""

    def __init__(self, ai_settings, screen):
        """
		Initializes the alien and sets the starting position
		"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        """
		Draw the alien at its current location
		"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """
		Checks if alien is at edge of screen, returns `True`
		"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left < 0:
            return True

    def update(self):
        """
		Moves the alien right or left
		"""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x
