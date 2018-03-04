# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 21:51:03 2018

@author: Administrator
"""

class Settings():
    
    def __init__(self):
        # 屏幕
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (100,149,237)
        
        #飞船
        #self.ship_speed_factor = 1.5
        self.ships_limit = 3
        
        #子弹
        #self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 5
        
        #外星人
        #self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.speedup_scale = 1.1
        self.fleet_direction = 1
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1
        self.alien_point = 50
        
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_point = int(self.alien_point * self.speedup_scale)
        #test# print(self.alien_point)
        
        
        
        