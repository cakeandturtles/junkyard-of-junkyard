using System;

namespace RPG{
  class Program{
    
    ///////////////////////////INITIALIZE PUBLIC VARIABLES!!////////////////////////////////////
    public static string command;
    public static string[] commands;
    public static string[] verbarray;
    public static int whereAmI;
    public static int gibberish;
    public static bool game;
    ////////////////////////////////////////////////////////////////////////////////////////////
    public static void Main(string[]args){
      game = true;
      whereAmI=0;
      gibberish=0;
      verbarray = new string[10];
      verbarray[0] = "run"; 
      verbarray[1] = "sword";
      verbarray[2] = "shield";
      verbarray[3] = "spellbook";
      verbarray[4] = "arrow";
      verbarray[5] = "steal";
      verbarray[6] = "heal";
      verbarray[7] = "bomb";
      verbarray[8] = "boomerang";
      verbarray[9] = "flute";
      Console.Clear();
      Console.WriteLine("The air is smoldering. You are sprinting.");
      Console.WriteLine("Sweat drips heavily down your brow.");
      Console.WriteLine("You clench a shining sword in your right fist.");
      Console.WriteLine("In your left is an open spellbook.");
      Console.WriteLine("Your bag is filled with assortments of magic items and weapons.");
      Console.WriteLine("The heat from the fires on either side of you is making you feel weak.");
      Console.WriteLine("A roar is heard as a new wall of flame encircles your path.");
      Console.WriteLine("You turn around to face the dragon from which the roar and fire erupted.");
      Console.WriteLine();
      Console.WriteLine("What is your command?");
      foreach(string i in verbarray){
        Console.Write(i);Console.Write(" ");}
      while(game==true){
        Console.Write("\n>>");
        commandChecker();}
    }

//////////////////////////////////////////////////////////////////////////////////////////////////////////////
    public static void commandChecker(){
      command = Console.ReadLine();
      commands = command.Split(' ');
      Console.WriteLine();
      switch(commands[0]){
        case "run": case "RUN": case "Run":
          break;
        case "sword": case "SWORD": case "Sword":
          break;
        case "shield": case "SHIELD": case "Shield":
          break;
        case "spellbook": case "SPELLBOOK": case "Spellbook": case "SpellBook":
          break;
        case "arrow": case "ARROW": case "Arrow":
          break;
        case "steal": case "STEAL": case "Steal":
          break;
        case "heal": case "HEAL": case "Heal":
          break;
        case "bomb": case "BOMB": case "Bomb":
          break;
        case "boomerang": case "BOOMERANG": case "Boomerang":
          break;
        case "flute": case "FLUTE": case "Flute":
          break;
        default:
          Default();
          break;      
      }
    }

/////////////////////////////////////////////////////////////////////////////////

  public static void Default(){
    if (gibberish == 0){
      Console.WriteLine("You shout gibberish at the dragon. \nIt is momentarily stunned.");
      gibberish+=1;}
    else if (gibberish == 1){
      Console.WriteLine("\""+commands[0]+"\", you shout! \nThe dragon's patience seems to be wearing thin.");
      gibberish+=1;}
    else if (gibberish == 2){
      Console.WriteLine("The dragon is not having any more of your nonsense.");
      Console.WriteLine("He promptly eats you while you scream wildly at him.");
      Console.WriteLine("You have died.");
      game = false;}
    }
  }
}
