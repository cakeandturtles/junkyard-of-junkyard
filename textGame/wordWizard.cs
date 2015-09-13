using System;

namespace wordWizard{
  class Program{

    ///////////INITIALIZE VARIABLES///////////////////////////////////
    public static string command; //declares variable for player input
    public static int mapHeight= 15;
    public static int mapWidth = 20;
    public static char[][] gameMap = new char[mapHeight][]; //an array to hold the map
    //////////////////////////////////////////////////////////////////

    public static void Main(string[]args){ //Entry point for the game 

      Console.Clear();
      for (int i = 0; i < mapHeight; i++){
        gameMap[i] = new char[mapWidth];
        for (int j = 0; j < mapWidth; j++){
          gameMap[i][j] = '@'; 
          Console.Write(gameMap[i][j]);
          Console.Write(' ');
          if (j==mapWidth-1){ Console.Write("\n"); } } }
      Console.WriteLine("Hello, world.");

      while(true){ //Game loop
        Console.Write(">>");
        command = Console.ReadLine();
        Console.Clear();
 
        for (int i = 0; i < mapHeight; i++){
          for (int j = 0; j < mapWidth; j++){
            Console.Write(gameMap[i][j]);
            Console.Write(' '); 
            if (j==mapWidth-1){ Console.Write("\n"); } } }
      }
    }
  }
}
    

