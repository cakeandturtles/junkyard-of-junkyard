def Gravity(self,solidSet):
  self.rect.y+=self.yVel

  if self.whereAmI==0 and self.yVel<=self.yMax:
    self.yVel+=self.yAcc
  elif self.yVel>self.yMax: ##Sets a limit on yVelocity
    self.yVel=self.yMax

  for i in solidSet: 
    if self.rect.move(0,self.yVel).colliderect(i.rect) or self.rect.move(0,1).colliderect(i.rect): ##If either player velocity or player mass collides with ground
      self.collision=1 
      if self.rect.move(0,self.yVel).colliderect(i.rect) and not self.rect.move(0,1).colliderect(i.rect): ##If player's velocity collides with ground but not player's mass
        while not self.rect.move(0,1).colliderect(i.rect): ##While the mass is not touching the ground
          self.rect.y+=1 ##Move the mass downward

  if self.collision!=1:
    self.whereAmI=0 ##Player is in the air
  else:
    self.whereAmI=1 ##Player is touching the ground
    self.yVel=0

  self.collision=0
