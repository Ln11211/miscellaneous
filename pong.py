'''
Copyright (C) 2023 M.L.N.Rao(Ln11211) - All Rights Reserved
 * You may use, distribute and modify this code under the
 * terms of the LNCODE license, which unfortunately won't be
 * written for another century.
 *
 * You should have received a copy of the LNCODE license with
 * this file. If not, please write to:Ln11211.
'''

import pygame
import random

pygame.init()

#Window properties and flags
width,height=1000,600
pygame.display.set_caption("PING PONG")
window=pygame.display.set_mode((width,height))
run=True
direction = [0,1]
angle=[0,1,2]
player_1=player_2=0

#colors used
BLACK=(0,0,0)
RED=(255,0,0)
BLUE=(0,0,255)
WHITE=(225,225,225)

#Ball properties
rad=15
ball_x,ball_y= (width/2)-rad, (height/2)-rad
ball_vel_x, ball_vel_y= 0.85 , 0.85

#Paddle properties
paddle_wid,paddle_heig=20,120
left_y=right_y=(height/2)-(paddle_heig/2)
left_x,right_x= 100- (paddle_wid/2) , width- (100- (paddle_wid/2))
right_pad_vel,left_pad_vel=0,0


while run:
    window.fill(BLACK)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run=False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                right_pad_vel= -1.2
            if i.key == pygame.K_DOWN:
                right_pad_vel= 1.2
            if i.key == pygame.K_w:
                left_pad_vel= -1.2
            if i.key == pygame.K_s:
                left_pad_vel=1.2
        
        if i.type == pygame.KEYUP:
            right_pad_vel=0
            left_pad_vel=0
    
    
    #Ball-Wall Collision conditions
    #############
    if ball_y <= 0+rad or ball_y >= height-rad:
        ball_vel_y*=-1

    if ball_x >= width-rad:
        ball_x,ball_y= (width/2)-rad, (height/2)-rad
        player_1+=1
        
        dir=random.choice(direction)
        ang=random.choice(angle)
        if dir ==0:
            if ang==0:
                ball_vel_x,ball_vel_y = -1.4, 1
            if ang==1:
                ball_vel_x,ball_vel_y = -1, 1
            if ang==2:
                ball_vel_x,ball_vel_y = -1, 1.4
        
        if dir ==1:
            if ang==0:
                ball_vel_x,ball_vel_y = 1.4, 1
            if ang==1:
                ball_vel_x,ball_vel_y = 1, 1
            if ang==2:
                ball_vel_x,ball_vel_y = 1, 1.4
        
        #ball_vel_x*=-1

    if ball_x <= 0+rad:
        ball_x,ball_y= (width/2)-rad, (height/2)-rad
        ball_vel_x,ball_vel_y=0.85,0.85
        player_2+=1

        dir=random.choice(direction)
        ang=random.choice(angle)
        if dir ==0:
            if ang==0:
                ball_vel_x,ball_vel_y = -1.4, 1
            if ang==1:
                ball_vel_x,ball_vel_y = -1, 1
            if ang==2:
                ball_vel_x,ball_vel_y = -1, 1.4
        if dir ==1:
            if ang==0:
                ball_vel_x,ball_vel_y = 1.4, 1
            if ang==1:
                ball_vel_x,ball_vel_y = 1, 1
            if ang==2:
                ball_vel_x,ball_vel_y = 1, 1.4
    ##############

    #Paddle movement
    ##############
    if left_y > height-paddle_heig:
        left_y = height-paddle_heig
    if  left_y < 0:
        left_y = 0

    if right_y > height-paddle_heig:
        right_y= height-paddle_heig
    if  right_y < 0:
        right_y = 0
    ##############

    #Paddle-Ball collision
    ##############
    if left_x <= ball_x <= left_x+paddle_wid:
        if left_y <= ball_y <= left_y+paddle_heig:
            ball_x=left_x+paddle_wid
            ball_vel_x*=-1

    if right_x <= ball_x <= right_x+paddle_wid:
        if right_y <= ball_y <= right_y+paddle_heig:
            ball_x=right_x
            ball_vel_x*=-1
    ##############

    #Ball movement
    ##############
    ball_x+=ball_vel_x
    ball_y+=ball_vel_y
    right_y+=right_pad_vel
    left_y+=left_pad_vel
    ##############

    #Scoreboard
    font=pygame.font.SysFont('callibri',32)
    score=font.render('player 1:- '+str(player_1*10),True,WHITE)
    window.blit(score,(25,25))

    score=font.render('player 2:- '+str(player_2*10),True,WHITE)
    window.blit(score,(825,25))

    pygame.draw.circle(window,RED,(ball_x,ball_y),rad)
    pygame.draw.rect(window,BLUE,pygame.Rect(left_x,left_y,paddle_wid,paddle_heig))
    pygame.draw.rect(window,BLUE,pygame.Rect(right_x,right_y,paddle_wid,paddle_heig))

    win_font=pygame.font.SysFont('callibri',100)
    if player_1 >=5:
        window.fill(BLACK)
        endscreen=win_font.render('Player 1 WON !!!',True,WHITE)
        window.blit(endscreen,(200,250))
    if player_2 >=5:
        window.fill(BLACK)
        endscreen=win_font.render('Player 2 WON !!!',True,WHITE)
        window.blit(endscreen,(200,250))
    pygame.display.update()