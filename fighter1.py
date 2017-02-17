import pygame, sys
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Fighter")
screen = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()
fighter_image = pygame.image.load("images/fighter.png").convert()
fighter_image.set_colorkey((255,255,255))

class Fighter:
 def __init__(self):
  self.x = 450
  self.y = 270
  
 def draw(self):
  screen.blit(fighter_image,(self.x,self.y))
  
fighter = Fighter()

while 1:
 clock.tick(60)
 
 for event in pygame.event.get():
  if event.type == QUIT:
   sys.exit()
   
   screen.fill((0,0,0))
   fighter.draw()
   
   pygame.display.update()