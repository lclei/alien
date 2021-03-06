# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 21:56:28 2018

@author: Administrator
"""
# game_functions

import sys
from time import sleep

import pygame
from bullet import Bullet
from alien import Alien

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:            
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
    
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    
def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False  

def check_events(ai_settings,stats,play_button,screen,scoreboard,ship,aliens,bullets,):
    """响应鼠标和按键事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,stats,play_button,screen,scoreboard,ship,aliens,bullets,mouse_x,mouse_y)
       
def check_play_button(ai_settings,stats,play_button,screen,scoreboard,ship,aliens,bullets,mouse_x,mouse_y):
    if play_button.rect.collidepoint(mouse_x,mouse_y) and not stats.game_active:
        pygame.mouse.set_visible(False)
        ai_settings.initialize_dynamic_settings()
        stats.reset_stats()
        stats.game_active = True
        
        scoreboard.prep_score()
        scoreboard.prep_high_score()
        scoreboard.prep_level()
        scoreboard.prep_ships()
        
        aliens.empty()
        bullets.empty()        
        creat_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()    
    
    
def update_screen(ai_settings,stats,screen,scoreboard,ship,aliens,bullets,play_button):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    scoreboard.show_score()
    if not stats.game_active:        
        play_button.draw_button()
    pygame.display.flip()
    
def update_bullets(ai_settings, stats, screen, scoreboard, ship, aliens, bullets):
    bullets.update()
    #删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_collision(ai_settings, stats, screen, scoreboard, ship, aliens, bullets)
    
def check_collision(ai_settings, stats, screen, scoreboard, ship, aliens, bullets):
    
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
    if collisions:
        for aliens in collisions.values():
            """碰撞检测返回字典collisions，对字典里的所有外星人遍历，统计分数"""
            stats.score += ai_settings.alien_point * len(aliens)
            scoreboard.prep_score()
        check_high_score(stats,scoreboard)
    
    if len(aliens) == 0:
        print("你消灭了所有外星飞船！啊！ 又来一批！")
        bullets.empty()
        ai_settings.increase_speed()
        
        stats.level += 1
        scoreboard.prep_level()
        creat_fleet(ai_settings, screen, ship, aliens)
        
            
def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可以容纳多少外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = ai_settings.screen_height - (3*alien_height) -ship_height
    number_rows = int(available_space_y/2/alien_height)
    return number_rows
    
def creat_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人，放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)

def creat_fleet(ai_settings, screen, ship, aliens):
    """创建舰队"""    
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width) 
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            creat_alien(ai_settings, screen, aliens, alien_number,row_number)
            
def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
        
        
def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_aliens_bottom(ai_settings, stats, screen,scoreboard, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen,scoreboard, ship, aliens, bullets)
            break

def update_aliens(ai_settings, stats, screen,scoreboard, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update(ai_settings)
    
    if pygame.sprite.spritecollideany(ship, aliens):
        print("飞船撞毁！")
        ship_hit(ai_settings, stats, screen,scoreboard, ship, aliens, bullets)
    
    check_aliens_bottom(ai_settings, stats, screen,scoreboard, ship, aliens, bullets)
        
def ship_hit(ai_settings, stats, screen,scoreboard, ship, aliens, bullets):
    if stats.ships_left > 0:        
        stats.ships_left -=1  
        scoreboard.prep_ships()
        aliens.empty()
        bullets.empty()        
        creat_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()        
        sleep(0.5)
    else:
        stats.game_active =False
        pygame.mouse.set_visible(True)
        
def check_high_score(stats,scoreboard):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scoreboard.prep_high_score()
        
    