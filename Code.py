import pygame
from pygame import  mixer
import time
import math
pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Turtle Race")
icon = pygame.image.load("animal.png")
pygame.display.set_icon(icon)
# Player 1
Player = pygame.image.load("animal.png")
playerX = 550
playerY = 300
# Player 2
Player2 = pygame.image.load("turtle.png")
Player2X = 550
Player2Y = 175

# Flag
Flag = pygame.image.load("Finish.png")
FlagX = 0
FlagY = 50
# Title
Title = pygame.image.load("Titles.png")
TitleX = 150
TitleY = 50
# Winning
Win = pygame.image.load("Win.png")
WinX = -100
WinY = -100
Win2 = pygame.image.load("Win2.png")
Win2X = -100
Win2Y = -100
# Hint
Hint = pygame.image.load("Hintss.png")
HintX = -500
HintY = -500
# Flower
Flower = pygame.image.load("Flower.png")
FlowerX = 250
FlowerY = 0
# Rock
Rock = pygame.image.load("Rock.png")
RockX = -500000
RockY = -5000000
Rock_change = 0.1
# Cube
Cubey = pygame.image.load("C.png")
# Butterfly
Butterfly = pygame.image.load("Butterfly.png")



def Sounds():
    Sound = mixer.Sound("Jump.wav")
    Sound.play()


#Level
B = 255
G = 0
R = 0
a = True
b = 1
c = 2

mixer.music.load("AA.wav")
mixer.music.play(-1)

def player():
    screen.blit(Player,(playerX, playerY))


def player2():
    screen.blit(Player2, (Player2X, Player2Y))


def flag():
    screen.blit(Flag, (FlagX, FlagY))

def title():
    screen.blit(Title, (TitleX, TitleY))

def win():
    screen.blit(Win , (WinX, WinY))

def win2():
    screen.blit(Win2 , (Win2X, Win2Y))

def hint():
    screen.blit(Hint , (HintX, HintY))

def flower(X, Y):
    screen.blit(Flower, (X, Y))

def Cube(X, Y):
    screen.blit(Cubey , (X, Y))

def Butterflies(X, Y):
    screen.blit(Butterfly , (X, Y))

def rock():
    screen.blit(Rock , (RockX, RockY))

def collision():
    distance = math.sqrt(math.pow(playerX-FlowerX,2) + math.pow(playerY-FlowerY,2))
    if distance < 27:
      return True
    else:
      return False


def collision2():
    distance = math.sqrt(math.pow(Player2X-RockX,2) + math.pow(Player2Y-RockY,2))
    if distance < 27:
      return True
    else:
      return False



running = True

while running:




   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and a == True:
                playerX -= 3
                Sounds()
                TitleY = -1000
                print(FlowerY)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Key Pressed Escape")
                pygame.quit()


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and a == True:
                Player2X -= 3
                Sounds()
                TitleY = -1000

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and a == False:
                playerX = 550
                playerY = 300
                Player2X = 550
                Player2Y = 150
                WinY = -1000
                Win2Y = -1000
                HintY = -1000
                HintX = -1000
                RockX = 200
                RockY = 10
                RockY += Rock_change
                a = True
                b = 1
                c = 1
                B -= 125
                G += 125
                print(B)
            pygame.display.update()

        if B < 0 or G > 255 or R > 255:
           G = 255
           B = 0
           R += 255

        if R > 255:
            R = 255

        if playerX <= 10:
            a = False
            WinX = 150
            WinY = 10
            HintX = 150
            HintY = 100


        if Player2X <= 10:
            a = False
            Win2X = 150
            Win2Y = 10
            HintX = 150
            HintY = 100


        if b == 1 and a == False:
             sound = mixer.Sound("Finish.wav")
             sound.play()
             b = 2







   screen.fill((R, G, B))

   if RockY < 800:
       RockY = 15



   RockY += Rock_change



   player()
   player2()
   flag()
   title()
   win()
   win2()
   hint()
   flower(FlowerX, FlowerY)
   flower(200, 0)
   flower(150, 0)
   flower(100, 0)
   flower(50, 0)
   flower(0, 0)
   flower(300, 0)
   flower(350, 0)
   flower(400, 0)
   flower(450, 0)
   flower(500, 0)
   flower(550, 0)
   flower(200, 338)
   flower(150, 338)
   flower(100, 338)
   flower(50, 338)
   flower(0, 338)
   flower(300, 338)
   flower(350, 338)
   flower(400, 338)
   flower(450, 338)
   flower(500, 338)
   flower(550, 338)
   flower(250, 338)
   Butterflies(550, 325)
   pygame.display.update()
