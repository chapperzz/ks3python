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
  self.x = screen.get_width()/2 -fighter_image.get_width()/2
  self.y = screen.get_height()-(fighter_image.get_width()/2 +fighter_image.get_height()/2)
  self.dir = 0
  
 def turn(self):
  if pressed_keys[K_a] and self.dir < 90:
   self.dir +=1
  if pressed_keys[K_z] and self.dir > -90:
   self.dir +=-1
  
 def draw(self):
  rotated = pygame.transform.rotate(fighter_image,self.dir)
  screen.blit(rotated,(self.x+fighter_image.get_width()/2-rotated.get_width()/2, self.y+fighter_image.get_height()/2-rotated.get_height()/2))
  
fighter = Fighter()

while 1:
 clock.tick(60)
 
 for event in pygame.event.get():
  if event.type == QUIT:
   sys.exit()
   
 pressed_keys = pygame.key.get_pressed()
   
 screen.fill((0,0,0))
 fighter.draw()
 fighter.turn()
   
 pygame.display.update()