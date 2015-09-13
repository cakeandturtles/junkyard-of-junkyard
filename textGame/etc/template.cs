using System;

namespace demo{
  class Program{
    
    ///////////INITIAL VARIABLES!!!!!!!/////////////////////////////////
    public static string[] verbarray; //creates array of available verbs 
    public static string command; //declares variable for player input
    public static string[] commands;
    public static int whereAmI;
    ////////////////////////////////////////////////////////////////////


    public static void Main(string[]args){ ////////ENTRY POINT FOR GAME
     
      verbarray = new string[3];
      verbarray[0] = "look";
      verbarray[1] = "grab";
      verbarray[2] = "walk";
      whereAmI=0;
      Console.Clear();
      Console.WriteLine("Hello, world.");
      while(true){ //Game loop
        if (whereAmI==0){
          Console.Write(">>");
          commandChecker();}
      } 
    }
///////////////////////////////////////////////////////////////////////////////////////////

    public static void commandChecker(){ //Player input checker
      command = Console.ReadLine();
      commands = command.Split(' ');
      Console.WriteLine();
      switch (commands[0]){
        case "a":
        case "A":
        case "action":
        case "Action":
        case "actions":
        case "Actions":
          Lex();
          break;

        case "look":
        case "Look":
          Look();
          break;

        case "grab":
        case "Grab":
          Grab();
          break;

        case "walk":
        case "Walk":
          Walk();
          break;

        case "info":
        case "Info":
          Info();
          break;

        default:
          Console.WriteLine("Command unavailable.");
          break;
      }
    }

///////////////////////////////////////////////////////////////////////////
    public static void Inv(){
      //This will be the inventory of tangible items available to character
    }
//////////////////////////////////////////////////////////////////////////////

    public static void Lex(){
      //This will be the dictionary of available verbs the player may use
      Console.Clear();
      Console.WriteLine("The following verbs are available for use:");
      Console.WriteLine();
      foreach(string verb in verbarray){
        Console.WriteLine(verb);}
      Console.WriteLine();
      Console.WriteLine("For an explanation of the action, type \"info\" followed by a space and the action in question, and press return.");
    }
///////////////////////////////////////////////////////////////////////////////
  
    public static void Info(){
      switch(commands[1]){
        case "look":
        case "Look":
          Console.WriteLine("\"look\" may or may not take an object.");
          Console.WriteLine("If an object is given, I will focus on the given object.");
          Console.WriteLine("If no object is given, I will survey the general area.");
          Console.WriteLine("In either case I will report what is seen to you.");
          break;
     
        case "grab":
        case "Grab":
          Console.WriteLine("\"grab\" must take an object.");
          Console.WriteLine("I would not know what to grab otherwise.");
          Console.WriteLine("If an object is given, I will attempt to take it into possession manually.");
          break;
 
        case "walk":
        case "Walk":
          Console.WriteLine("\"walk\" must be followed by a direction.");
          Console.WriteLine("Either \"north\", \"south\", \"east\", or \"west\".");
          Console.WriteLine("I will walk in the direction given, if possible");
          break;
 
        default:
          Console.WriteLine("I'm sorry, I do not know that action.");
          break;
      }
    }
////////////////////////////////////////////////////////////////////////////
       
    public static void Look(){
      if(whereAmI==0){

          if (commands.Length==2 && commands[1]!=""){
            switch(commands[1]){
              default:
                Console.WriteLine("I cannot see that.");
                break;}}
          else if (commands.Length==1 || (commands.Length==2 && commands[1]=="")){
            Console.WriteLine("There is a door to the north.");}
          else{Console.WriteLine("I can only accept simple commands.");}

      }

    }

///////////////////////////////////////////////////////////////////////////////
    public static void Grab(){
      if (whereAmI==0){
        if (commands.Length==2 && commands[1]!=""){
          Console.WriteLine();
        }
        else if (commands.Length==1 || (commands.Length==2 && commands[1]=="")){
          Console.WriteLine("I must have an object to grab.");}
        else{Console.WriteLine("I can only accept simple commands.");}
      }
    }
//////////////////////////////////////////////////////////////////////

    public static void Walk(){
      
      if (commands.Length==2 && commands[1]!=""){
        switch(commands[1]){
          case "North": case "north": case "forward": case "Forward":
            Console.WriteLine("North");
            break;
          case "South": case "south": case "backward": case "Backward":
            Console.WriteLine("South");
            break;
          case "East": case "east": case "right": case "Right":
            Console.WriteLine("East");
            break;
          case "West": case "west": case "left": case "Left":
            Console.WriteLine("West");
            break;
          default:
            Console.WriteLine("default");
            break;}}
      else if (commands.Length==1 || (commands.Length==2 && commands[1]=="")){
        Console.WriteLine("I must have a direction in which to walk.");}
      else{Console.WriteLine("I can only accept simple commands.");}
    }
////////////////////////////////////////////////////////////////////////

  }
}
