import os,sys
import charVar
import random

confusedList = ["Huh?", "What?", "Uh...", "I don't follow", "fdsfgs", "Sorry what?", "wut", "Ya wanna run that by me again?", "I'm going to pretend you didn't say that.", "Try again...", "Concentrate and ask again.", "No, I'm not doing that.", "Who?", "How?", "No thanks.", "Command unavailable"]

def Look(objectL):
  if not objectL:
    print "There is something strange about the bear."
  else:
    if objectL == "at":
      print "WHAT ARE YOU TRYING TO LOOK AT?!"
    if objectL == "bear":
      print "There is something strange about that bear."
    else: 
      print confusedList[random.randint(0,len(confusedList)-1)]

def Walk(direction):
  if direction=="north":
    print "NORTH"
  elif direction == "south":
    print "SOUTH"
  elif direction == "west":
    print "WEST"
  elif direction == "east":
    print "EAST"
  else:
    print "ELSE"
  
