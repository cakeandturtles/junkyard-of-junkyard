import os, sys
import charVar
import action
import random

def commandChecker():
  commandList=raw_input().lower().split(' ')
  print

  if commandList[0] == "a" or commandList[0] == "action" or commandList[0] == "actions":
    Lex()

  elif commandList[0] == "look":
    if len(commandList)==3:
      if commandList[1] == "at":
        action.Look(commandList[2])
    elif len(commandList)==2:
      action.Look(commandList[1])
    elif len(commandList)>3:
      print "Please only input one object."
    else:
      action.Look(None)

  elif commandList[0] == "walk":
    if len(commandList)!=2:
      print "Please insert an a direction"
    else:
      action.Walk(commandList[1])

  else:
    print action.confusedList[random.randint(0,len(action.confusedList)-1)]
  
def Lex():
  os.system('cls' if os.name=='nt' else 'clear')
  print "The following verbs are available for use:"
  indentter=0
  for i in charVar.verbList:
    if indentter%9==0:
      print "\n"
    print i,
    indentter+=1
  print "\n"
