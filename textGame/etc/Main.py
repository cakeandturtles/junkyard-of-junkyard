import os, sys
import charVar
import commandChecker

os.system('cls' if os.name=='nt' else 'clear')
print "Welcome to the game!"
while True:
  print "You are being chased by a bear."
  print "Command?"
  print "\n>>",
  commandChecker.commandChecker()
