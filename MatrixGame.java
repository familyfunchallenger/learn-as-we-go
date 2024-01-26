import java.util.Random;
import java.util.Scanner;

public class MatrixGame {

  int[][] integerGrid;
  int[] playersScores;
  int[] playerInput;
  int[] topThreeRows;
  int[] topThreeCols;
  boolean isFirstTurn;
  boolean isLastTurn;
  boolean playerOneStartsFirst;
  boolean currentTurnIsPlayerOne;
  Scanner scanner;

  // initialize all the member variables.
  MatrixGame() {
    // Initialize the random 7x7 grid
    integerGrid = generateIntegerGrid();

    // Randomly decide if player 1 shall start or not
    Random random = new Random();
    playerOneStartsFirst = random.nextBoolean();

    // Record if current turn should be Player 1 or not
    currentTurnIsPlayerOne = playerOneStartsFirst;

    // Initialize the flag for first turn and last turn
    isFirstTurn = true;
    isLastTurn = false;

    topThreeRows = new int[3];
    topThreeCols = new int[3];

    playerInput = new int[4];
    playersScores = new int[2];

    scanner = new Scanner(System.in);
  }

  // Generate a 7x7 grid of integers (0-9)
  static int[][] generateIntegerGrid() {
    int rows = 7;
    int cols = 7;
    int[][] randomArray = new int[rows][cols];
    Random random = new Random();

    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
        randomArray[i][j] = random.nextInt(10); // Generates random integers between 0 and 9
      }
    }

    return randomArray;
  }

  // Parse and sanity check palyer inputs
  // If user input is invalid, return false; otherwise return true
  // This method will also store the 4 integers user enters into
  // playerInput array
  Boolean parsePlayerInput(String inputStr) {
    // First, get the four digits
    extractDigits(inputStr);
    // Next, check if the two coordinates are next to each other
    if (isGameEnd() ||
        (Math.abs(playerInput[0] - playerInput[2]) == 1
            && playerInput[1] == playerInput[3])
        || (Math.abs(playerInput[1] - playerInput[3]) == 1
            && playerInput[0] == playerInput[2])) {
      return true;
    }

    return false;
  }

  void extractDigits(String inputStr) {
    // Split the input string based on whitespace
    String[] digitStrings = inputStr.split("\\s+");

    // Convert each substring to an integer and store it in the array
    for (int i = 0; i < 4; i++) {
      Integer.parseInt(digitStrings[i]);
      playerInput[i] = Integer.parseInt(digitStrings[i]);
    }
  }

  // Find top three rows
  void findTopThreeRows() {
    int[] rowSums = new int[integerGrid.length];

    for (int i = 0; i < integerGrid.length; i++) {
      int sum = 0;
      for (int j = 0; j < integerGrid[i].length; j++) {
        sum += integerGrid[i][j];
      }
      rowSums[i] = sum;
    }

    // Sort rowSums and get the indices of the top 3 sums
    for (int i = 0; i < 3; i++) {
      int maxIndex = 0;
      for (int j = 1; j < rowSums.length; j++) {
        if (rowSums[j] > rowSums[maxIndex]) {
          maxIndex = j;
        }
      }
      topThreeRows[i] = maxIndex;
      rowSums[maxIndex] = Integer.MIN_VALUE; // Mark the maximum as processed
    }
  }

  // Find top three columns
  void findTopThreeColumns() {
    int[] colSums = new int[integerGrid[0].length];

    for (int i = 0; i < integerGrid[0].length; i++) {
      int sum = 0;
      for (int j = 0; j < integerGrid.length; j++) {
        sum += integerGrid[j][i];
      }
      colSums[i] = sum;
    }

    // Sort colSums and get the indices of the top 3 sums
    for (int i = 0; i < 3; i++) {
      int maxIndex = 0;
      for (int j = 1; j < colSums.length; j++) {
        if (colSums[j] > colSums[maxIndex]) {
          maxIndex = j;
        }
      }
      topThreeCols[i] = maxIndex;
      colSums[maxIndex] = Integer.MIN_VALUE; // Mark the maximum as processed
    }
  }

  // Calculate players' scores
  // This calculation will be based on the top 3 rows and columns deteced
  void calculatePlayersScores() {
    playersScores[0] = 0;
    playersScores[1] = 0;
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 7; j++) {
        playersScores[0] = playersScores[0] + integerGrid[topThreeRows[i]][j];
        playersScores[1] = playersScores[1] + integerGrid[j][topThreeCols[i]];
      }
    }
  }

  // Print out curren matrix in a 9x9 way with markers to indicate the top 3 rows
  // and columns
  void printMatrix() {
    findTopThreeColumns();
    findTopThreeRows();
    System.out.println("  1 2 3 4 5 6 7");
    for (int i = 0; i < 7; i++) {
      System.out.print("1 ");
      for (int j = 0; j < 7; j++) {
        System.out.print(String.format("%d ", integerGrid[i][j]));
      }
      // Now print a "*" if this row is one of the top rows
      if (isOneOfTopThreeRows(i)) {
        // Current row is one of the top 3 rows, print a "*"
        System.out.println("*");
      } else {
        // It is not one of the top 3 rows, new line only
        System.out.println();
      }
    }
    // Print the indicators of the top 3 columns
    System.out.print(" ");
    for (int i = 0; i < 7; i++) {
      if (isOneOfTopThreeColumns(i)) {
        System.out.print("* ");
      } else {
        System.out.print(" ");
      }
    }
    System.out.println();
  }

  boolean isOneOfTopThreeRows(int row) {
    for (int i = 0; i < topThreeRows.length; i++) {
      if (row == topThreeRows[i]) {
        return true;
      }
    }
    return false;
  }

  boolean isOneOfTopThreeColumns(int col) {
    for (int i = 0; i < topThreeCols.length; i++) {
      if (col == topThreeCols[i]) {
        return true;
      }
    }
    return false;
  }

  // Get User Input for current turn
  // Need to update the currentTurnIsPlayerOne to keep a record
  // e.g. if current turn is for Player 1, at the end of this method,
  // currentTurnIsPlayerOne should
  // be truned to be false. If current turn is Player 2, at the end of this
  // method, currentTurnIsPlayerOne
  // should be turned to be true
  void getCurrentTurnInput() {

    if (currentTurnIsPlayerOne) {
      System.out.println("Player 1(row), it's your turn: ");
    } else {
      System.out.println("Player 2(col), it's your turn: ");
    }

    // Input: "Colummn first and then row: "
    System.out.print("Column first and then row: ");
    String inputStr = scanner.nextLine();
    while (!parsePlayerInput(inputStr)) {
      System.out.print("That's not a legal move. Try again: ");
      // get input into inputStr again.
      inputStr = scanner.nextLine();
    }
    currentTurnIsPlayerOne = !currentTurnIsPlayerOne;
  }

  // Dump out the final information
  void printFinalOutput() {
    calculatePlayersScores();
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
  void performSwapping() {
  }

  // Print out the player scores
  void printPlayersScores() {
    calculatePlayersScores();
    System.out.println(String.format("Player 1 score = %d", playersScores[0]));
    System.out.println(String.format("Player 2 score = %d", playersScores[1]));
  }

  boolean isGameEnd() {
    if (playerInput[0] == 0 && playerInput[1] == 0
        && playerInput[2] == 0 && playerInput[3] == 0) {
      return true;
    }
    return false;
  }

  // Main loop to interact with players
  void play() {
    // This is an infinite loop till a player gives the '0 0 0 0' input.
    while (!isLastTurn) {
      printMatrix();
      getCurrentTurnInput();
      isLastTurn = isGameEnd();
      if (isLastTurn) {
        printFinalOutput();
        printPlayersScores();
      } else {
        performSwapping();
        printPlayersScores();
      }
      // When the loop is executed at least once, we can safely mark
      // isFirstTurn as *false*
      isFirstTurn = false;
    }
    scanner.close();
  }

  public static void main(String args[]) {
    MatrixGame game = new MatrixGame();
    game.play();
  }

}
