# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 21:43:49 2018

@author: Administrator
"""


import pygame
from pygame.sprite import Group
from settings import Settings
from button import Button
from ship import Ship
from game_stats import GameStats
from scoreboard import ScoreBoard
#from alien import Alien
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings,screen,'Play')
    
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_settings)
    scoreboard = ScoreBoard(ai_settings,screen,stats)
    #alien = Alien(ai_settings,screen)
    gf.creat_fleet(ai_settings, screen, ship, aliens)
    
    while True:        
        gf.check_events(ai_settings,stats,play_button,screen,scoreboard,ship,aliens,bullets)
        if stats.game_active:            
            ship.update()
            gf.update_aliens(ai_settings, stats, screen,scoreboard, ship, aliens, bullets )
            gf.update_bullets(ai_settings, stats, screen, scoreboard, ship, aliens, bullets)                
        gf.update_screen(ai_settings,stats,screen,scoreboard,ship,aliens,bullets,play_button)

run_game()
