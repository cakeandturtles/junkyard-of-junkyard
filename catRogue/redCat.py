import os,sys
import pygame
import loader
import random
from pygame.locals import *

class redCat(pygame.sprite.Sprite):
  """I am the enemy."""
  def __init__(self,x,y):
    pygame.sprite.Sprite.__init__(self)
    self.rcf1 = pygame.transform.scale(loader.load_image("etc/redcatfront1.png",-1),(32,32))
    self.rcf2 = pygame.transform.scale(loader.load_image("etc/redcatfront2.png",-1),(32,32))
    self.rcb1 = pygame.transform.scale(loader.load_image("etc/redcatback1.png",-1),(32,32))
    self.rcb2 = pygame.transform.scale(loader.load_image("etc/redcatback2.png",-1),(32,32))
    self.rcl1 = pygame.transform.scale(loader.load_image("etc/redcatleft1.png",-1),(32,32))
    self.rcl2 = pygame.transform.scale(loader.load_image("etc/redcatleft2.png",-1),(32,32))
    self.rcr1 = pygame.transform.scale(loader.load_image("etc/redcatright1.png",-1),(32,32))
    self.rcr2 = pygame.transform.scale(loader.load_image("etc/redcatright2.png",-1),(32,32))
    self.image = self.rcf1
    self.rect = self.image.get_rect()
    self.rect.topleft = x*32,y*32
    self.updateimage=0
    self.collision=0
    self.direct='s'
    self.randomMove=0
    

  def update(self,target):
    ##FOR IMAGE UPDATING!!!
    if self.direct == 'n':
      if self.updateimage<=30:
        self.image = self.rcb1
      else: self.image = self.rcb2
    elif self.direct == 's':
      if self.updateimage<=30:
        self.image = self.rcf1
      else: self.image = self.rcf2
    elif self.direct == 'e':
      if self.updateimage<=30:
        self.image = self.rcr1
      else: self.image = self.rcr2
    elif self.direct == 'w':
      if self.updateimage<=30:
        self.image = self.rcl1
      else: self.image = self.rcl2
    self.updateimage+=1

    if self.updateimage>=60:
      self.updateimage=0

    ##FOR RANDOM MOVEMENT!!!
    if self.updateimage%30==0:
      self.randomMove=random.randint(0,4)
      if self.randomMove==0:###########
        self.direct = 'n'
        for i in target:
          if self.rect.move(0,-32).colliderect(i.rect):
            self.collision=1
        if self.collision!=1 and self.rect.y>0*32:
          self.rect.y-=32

      elif self.randomMove==1:##########
        self.direct='s'
        for i in target:
          if self.rect.move(0,32).colliderect(i.rect):
            self.collision=1
        if self.collision!=1 and self.rect.y<32*9:
          self.rect.y+=32

      elif self.randomMove==2:##########
        self.direct='w'
        for i in target:
          if self.rect.move(-32,0).colliderect(i.rect):
            self.collision=1
        if self.collision!=1 and self.rect.x>0*32:
          self.rect.x-=32

      elif self.randomMove==3:###########
        self.direct='e'
        for i in target:
          if self.rect.move(32,0).colliderect(i.rect):
            self.collision=1
        if self.collision!=1 and self.rect.x<9*32:
          self.rect.x+=32
    
      self.collision=0
