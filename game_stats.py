# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 10:22:21 2018

@author: Administrator
"""

class GameStats():
    
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True
        self.high_score = 0
        self.level = 1
        
    def reset_stats(self):
        self.ships_left = self.ai_settings.ships_limit
        self.score = 0
        self.level = 1
        