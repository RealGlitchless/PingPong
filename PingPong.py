import pygame
import sys
import os
from PIL import Image
import time
import ctypes
import random

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)

size = width, height = 700, 500
screen = pygame.display.set_mode(size)
screen.fill(black)
pygame.display.set_caption("Ping Pong")

root = os.path.dirname(sys.modules['__main__'].__file__)

ball = Image.open(root + "\\ball.png")
ballWidth = 25
ballHeight = 25
ball = ball.resize((ballWidth, ballHeight))
ball.save("ball.png")
ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
ballrect = ballrect.move(350, 220)

player1_line = Image.open(root + "\\white.png")
lineWidth = 20
lineHeight = 100
player1_line = player1_line.resize((lineWidth, lineHeight))
player1_line.save("line.png")
player1_line = pygame.image.load("line.png")
player1Rect = player1_line.get_rect()
player1Rect = player1Rect.move(20, 200)

player2_line = Image.open(root + "\\white.png")
lineWidth = 20
lineHeight = 100
player2_line = player2_line.resize((lineWidth, lineHeight))
player2_line.save("white.png")
player2_line = pygame.image.load("white.png")
player2Rect = player2_line.get_rect()
player2Rect = player2Rect.move(660, 200)

ballSpeed = [0, 0]
lineSpeed = [0, 2]


def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


def randDirection():
    ballSpeed[0] = -ballSpeed[0]
    if random.randint(0, 1) == 1:
        ballSpeed[1] = -ballSpeed[1]
    else:
        ballSpeed[1] = +ballSpeed[1]


noWinner = True
while noWinner:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(ballSpeed)
    player1Keys = pygame.key.get_pressed()
    player2Keys = pygame.key.get_pressed()

    if player1Keys[pygame.K_w]:
        if not player1Rect.top < 0:
            if lineSpeed[1] == 2:
                lineSpeed[1] = -lineSpeed[1]
                player1Rect = player1Rect.move(lineSpeed)

            else:
                player1Rect = player1Rect.move(lineSpeed)

    if player1Keys[pygame.K_s]:
        if not player1Rect.bottom > height:
            if lineSpeed[1] == -2:
                lineSpeed[1] = -lineSpeed[1]
                player1Rect = player1Rect.move(lineSpeed)

            else:
                player1Rect = player1Rect.move(lineSpeed)

    if player2Keys[pygame.K_UP]:
        if not player2Rect.top < 0:
            if lineSpeed[1] == 2:
                lineSpeed[1] = -lineSpeed[1]
                player2Rect = player2Rect.move(lineSpeed)

            else:
                player2Rect = player2Rect.move(lineSpeed)

    if player2Keys[pygame.K_DOWN]:
        if not player2Rect.bottom > height:
            if lineSpeed[1] == -2:
                lineSpeed[1] = -lineSpeed[1]
                player2Rect = player2Rect.move(lineSpeed)

            else:
                player2Rect = player2Rect.move(lineSpeed)

    if pygame.Rect.colliderect(player1Rect, ballrect):
        randDirection()

    if pygame.Rect.colliderect(player2Rect, ballrect):
        randDirection()

    if ballrect.top < 0 or ballrect.bottom > height:
        ballSpeed[1] = -ballSpeed[1]

    if ballrect.right > width:
        Mbox('Game Over', 'Player 1 wins!', 0)
        noWinner = False

    if ballrect.left < 0:
        Mbox('Game Over', 'PLayer 2 wins', 0)
        noWinner = False

    screen.fill(black)
    screen.blit(ball, ballrect)
    screen.blit(player1_line, player1Rect)
    screen.blit(player2_line, player2Rect)
    pygame.display.flip()

    time.sleep(0.002)
