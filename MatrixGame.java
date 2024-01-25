
public class MarixGame {

  Integer[][] integerGrid;
  Integer[] playerScores;
  Integer[] playerInput;
  Integer[] topThreeRows;
  Integer[] topThreeCols;
  Booelean isFirstTurn;
  Boolean isLastTurn;
  Boolean playerOneStartsFirst;
  Boolean currentTurnIsPlayerOne;

  // initialize all the member variables.
  MatrixGame() {
    
  }
  
  // Generate a 7x7 grid of integers (0-9)
  void generateIntegerGrid() {}

  // Parse and sanity check palyer inputs
  // If user input is invalid, return false; otherwise return true
  // This method will also store the 4 integers user enters into 
  // playerInput array
  Boolean parsePlayerInput(String input) {
    return false;
  }

  // Decide the top 3 rows 
  void findTopThreeRows() {}
  
  // Decide the top 3 columns
  void findTopThreeColumns() {}
  
  // Calculate players' scores
  // This calculation will be based on the top 3 rows and columns deteced
  void calculatePlayerScores() {
    
  }

  // Print out curren matrix in a 9x9 way with markers to indicate the top 3 rows and columns
  void printMatrix() {}

  // Get User Input for current turn
  // Need to update the currentTurnIsPlayerOne to keep a record 
  // e.g. if current turn is for Player 1, at the end of this method, currentTurnIsPlayerOne should
  // be truned to be false. If current turn is Player 2, at the end of this method, currentTurnIsPlayerOne
  // should be turned to be true
  void getCurrentTurnInput() {
    if (currentTurnIsPlayerOne) {
      System.out.println("Player 1(row), it's your turn: ");
    } else {
      System.out.println("Player 2(col), it's your turn: ");
    }

    // Input: "Colummn first and then row: "
    String inputStr = "";
    while (! parsePlayerInput(inputStr) {
      System.out.print("That's not a legal move. Try again: ");
      // get input into inputStr again.
    }
    currentTurnIsPlayerOne = !currentTurnIsPlayer;
  }

  // Dump out the final information
  void printFinalOutput() {
    if (playersScores[0] == playersScores[1]) {
      System.out.println("It's a tie");
    } else if (playersScores[0] > playersScores[1]) {
      System.out.println("Player 1 wins!");
    } else {
      System.out.println("Player 2 wins!");
    }
    System.out.println("Thanks for playing.");
  }

  // Perform the swapping based on the input from the current player
  void performSawapping() {}

  // Print out the player scores
  void printPlayersScores() {
    calculatePlayersScores();
    System.out.println("Player 1 score = %d", playersScores[0]);
    System.out.println("Player 2 score = %d", playersScores[1]);
  }
  
  // Main loop to interact with players
  Boolean play() {
    printMatrix();
    getCurrentTurnInput();
    if (isGameEnd()) {
      printFinalOutput()
    } else {
      performSwapping();
      printPlayersScores();
    }
  }

  public static void main(args[]) {
    MatrxGame game = new MatrixGame();
    game.play();
  }
  
}
