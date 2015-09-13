import os,sys

#########################DECLARE GLOBAL VARIABLES#####################
gibberish=0
whereAmI=0
######################################################################


def MainGame():
  verbList=("run", "sword", "shield", "spellbook", "arrow", "steal", "heal", "bomb", "boomerang", "flute")
  verbLine=""
  for i in verbList:
    verbLine+=i+" "
  os.system('cls' if os.name=='nt' else 'clear')
  print "The air is smoldering. You are sprinting."
  print "Sweat drips heavily down your brow."
  print "You clench a worn sword in your right fist."
  print "In your left is an open spellbook"
  print "Your bag is filled with assortments of magic items and weapons."
  print "The heat from the fires on either side of you is making you feel weak."
  print "A roar is heard as a new wall of flame encircles your path."
  print "You turn around to face the dragon from which the roar and fire erupted."
  print
  print "What is your command?"
  print verbLine
  while True:
    print "\n>>",
    commandChecker()


def commandChecker():
  command = raw_input()
  commandList = command.split(' ')
  print
  if commandList[0].lower()=="run": Run(commandList)
  elif commandList[0].lower()=="sword": Sword(commandList)
  elif commandList[0].lower()=="shield": Shield(commandList)
  elif commandList[0].lower()=="spellbook": Spell(commandList)
  elif commandList[0].lower()=="arrow": Arrow(commandList)
  elif commandList[0].lower()=="steal": Steal(commandList)
  elif commandList[0].lower()=="heal": Heal(commandList)
  elif commandList[0].lower()=="bomb": Bomb(commandList)
  elif commandList[0].lower()=="boomerang": Boomerang(commandList)
  elif commandList[0].lower()=="flute": Flute(commandList)
  else: Gibber(command)


def Gibber(commandLine):
  global gibberish
  if gibberish==0:
    print "You shout gibberish at the dragon. \nIt is momentarily stunned."
  elif gibberish==1:
    print "\"%s\", you shout! \nThe dragon's patience seems to be wearing thin."%(commandLine)
  else: 
    print "The dragon is not having any more of your nonsense."
    print "He promptly eats you while you scream wildly at him."
    print "You have died."
    sys.exit()
  gibberish+=1


def Run(commands):
  print "TODO: Run"

def Sword(commands):
  print "TODO: Sword"

def Shield(commands):
  print "TODO: Shield"

def Spell(commands):
  print "TODO: Spell"

def Arrow(commands):
  print "TODO: Arrow"

def Steal(commands):
  print "TODO: Steal"

def Heal(commands):
  print "TODO: Heal"

def Bomb(commands):
  print "TODO: Bomb"

def Boomerang(commands):
  print "TODO: Boomerang"

def Flute(commands):
  print "TODO: Flute"

##Calls the MainGame Function
MainGame()
