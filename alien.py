# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 22:40:02 2018

@author: Administrator
"""
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""
    
    def __init__(self,ai_settings,screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        self.image = pygame.image.load('image/alien2.png')
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    
    def update(self,ai_settings):
        self.x += (self.ai_settings.alien_speed_factor *
                       self.ai_settings.fleet_direction)
        self.rect.x = self.x