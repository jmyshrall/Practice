"""
File: game_stats.py
Collaborator: Justin Myshrall
Created: 9/28/2023
"""
class GameStats:
	"""
	Track statistics for Alien Invasion
	"""
	
	def __init__(self, ai_settings):
		"""
		Initialize statistics
		"""
		self.ships_left = None
		self.ai_settings = ai_settings
		self.reset_stats()
		self.game_active = False
		
	def reset_stats(self):
		"""
		Initialize statistics that can change during the game
		"""
		self.ships_left = self.ai_settings.ship_limit
