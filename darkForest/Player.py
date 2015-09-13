import os,sys
import pygame
import loader
import Gravity
import xMove
from pygame.locals import *

class Player(pygame.sprite.Sprite):
  """Wander"""
  def __init__(self,scale):
    pygame.sprite.Sprite.__init__(self)
    self.scale=scale
    self.image = pygame.transform.scale(loader.load_image("player/standRight1.png",-1),(27*scale,27*scale))
    self.facing='r'
    self.rect = self.image.get_rect()
    self.rect.topleft = 0,0
    self.collision=0

    ##Motion variables
    self.yVel=0
    self.yJump=(10.0/3.0)*scale
    self.yMax=(15.0/3.0)*scale
    self.yAcc=(0.5/3.0)*scale
    self.whereAmI=0
    self.isRight=0
    self.isLeft=0
    self.newLR="none"
    self.xVel=0
    self.xMax=(1.6)*scale
    self.xAcc=(0.8)*scale

    self.timer=1


  def PlaceMe(self,x,y):
    self.rect.topleft = x,y
    self.yVel=0
    self.whereAmI=0
 

  def update(self,solidSet):
    Gravity.Gravity(self,solidSet)
    xMove.xMove(self,solidSet)
    self.timer+=1
    if self.timer>60: self.timer=1


  def keyInput(self,keyPressed,keyReleased):
    if keyPressed == "jump":
      if self.whereAmI==1:
        self.yVel=-self.yJump

    if keyPressed == "right": 
      self.isRight=1
      self.newLR="right"
    elif keyReleased == "right": 
      self.isRight=0
      if self.isLeft==1: self.newLR="left"
      else: self.newLR="none"

    if keyPressed == "left": 
      self.isLeft=1
      self.newLR="left"
    elif keyReleased == "left": 
      self.isLeft=0 
      if self.isRight==1: self.newLR="right"
      else: self.newLR="none"
