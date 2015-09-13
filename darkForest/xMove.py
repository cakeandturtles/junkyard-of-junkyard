def xMove(self,solidSet):
  
  if self.newLR=="right":
    if self.xVel<0: self.xVel=0
    else: self.xVel+=self.xAcc
    if self.xVel>self.xMax: self.xVel=self.xMax

  if self.newLR=="left":
    if self.xVel>0: self.xVel=0
    else: self.xVel-=self.xAcc
    if self.xVel<-self.xMax: self.xVel=-self.xMax

  if self.newLR=="none":
    if self.xVel>self.xAcc: self.xVel-=self.xAcc
    elif self.xVel<-self.xAcc: self.xVel+=self.xAcc
    else: self.xVel=0




  if self.xVel>0:
    for i in solidSet:
      if self.rect.move(self.xVel,0).colliderect(i.rect) or self.rect.move(1,0).colliderect(i.rect):
        self.xVel=0
        if not self.rect.move(1,0).colliderect(i.rect):
          while not self.rect.move(1,0).colliderect(i.rect):self.rect.x+=1


  elif self.xVel<0:
    for i in solidSet:
      if self.rect.move(self.xVel,0).colliderect(i.rect) or self.rect.move(-1,0).colliderect(i.rect):
        self.xVel=0
        if not self.rect.move(-1,0).colliderect(i.rect):
          while not self.rect.move(-1,0).colliderect(i.rect):self.rect.x-=1


  if self.xVel>0: self.rect.x+=round(self.xVel)
  elif self.xVel<0: self.rect.x-=abs(round(self.xVel))
