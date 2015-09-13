import os,sys
import pygame
import loader
from pygame.locals import *

class playerCharacter(pygame.sprite.Sprite):
  """Wander"""
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.rmf1 = pygame.transform.scale(loader.load_image("redmonkeyfront1.png",-1),(32,32))
    self.rmf2 = pygame.transform.scale(loader.load_image("redmonkeyfront2.png",-1),(32,32))
    self.rmb1 = pygame.transform.scale(loader.load_image("redmonkeyback1.png",-1),(32,32))
    self.rmb2 = pygame.transform.scale(loader.load_image("redmonkeyback2.png",-1),(32,32))
    self.rml1 = pygame.transform.scale(loader.load_image("redmonkeyleft1.png",-1),(32,32))
    self.rml2 = pygame.transform.scale(loader.load_image("redmonkeyleft2.png",-1),(32,32))
    self.rmr1 = pygame.transform.scale(loader.load_image("redmonkeyright1.png",-1),(32,32))
    self.rmr2 = pygame.transform.scale(loader.load_image("redmonkeyright2.png",-1),(32,32))

    self.image = self.rmf1
    self.direct = 's'
    self.rect = self.image.get_rect()
    self.rect.topleft = 0*4,0*4
    self.updateimage=0
    self.collision=0

    self.rmStatlist=(10,1,1,5,5) #HADAM: HP, ATK, DEF, AGL, MAG
   

  def keyMove(self,hordirect,vertdirect,target):
    if vertdirect!=None:
      if vertdirect == "up":###########
        self.direct = 'n'
        for i in target:
          if self.rect.move(0,-2).colliderect(i.rect):
            self.collision=1
        if self.collision!=1 and self.rect.y>0*32:
          self.rect.y-=2

      elif vertdirect =="down":##########
        self.direct='s'
        for i in target:
          if self.rect.move(0,2).colliderect(i.rect):
            self.collision=1
        if self.collision!=1 and self.rect.y<32*9:
          self.rect.y+=2

      self.collision=0

    if hordirect!=None:
      if hordirect == "left":##########
        self.direct='w'
        for i in target:
          if self.rect.move(-2,0).colliderect(i.rect):
            self.collision=1
        if self.collision!=1 and self.rect.x>0*32:
          self.rect.x-=2

      elif hordirect == "right":###########
        self.direct='e'
        for i in target:
          if self.rect.move(2,0).colliderect(i.rect):
            self.collision=1
        if self.collision!=1 and self.rect.x<9*32:
          self.rect.x+=2
    
      self.collision=0


  def update(self,hordirect,vertdirect,target):
    ##FOR MOVEMENT
    self.keyMove(hordirect,vertdirect,target)

    ## FOR IMAGE UPDATING
    if self.direct == 'n':
      if self.updateimage<=30:
        self.image = self.rmb1
      else: self.image = self.rmb2
    elif self.direct == 's':
      if self.updateimage<=30:
        self.image = self.rmf1
      else: self.image = self.rmf2
    elif self.direct == 'e':
      if self.updateimage<=30:
        self.image = self.rmr1
      else: self.image = self.rmr2
    elif self.direct == 'w':
      if self.updateimage<=30:
        self.image = self.rml1
      else: self.image = self.rml2
    self.updateimage+=1

    if self.updateimage>=60:
      self.updateimage=0
      return
