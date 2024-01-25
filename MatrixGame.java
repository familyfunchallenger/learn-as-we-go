import java.util.Arrays;
import java.util.Random;

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
  int[][] generateRandomArray(int rows, int cols) {
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
  Boolean parsePlayerInput(String input) {
    return false;
  }

  
  // Find top three rows
  int[] findTopThreeRows(int[][] array) {
        int[] rowSums = new int[array.length];

        for (int i = 0; i < array.length; i++) {
            int sum = 0;
            for (int j = 0; j < array[i].length; j++) {
                sum += array[i][j];
            }
            rowSums[i] = sum;
        }

        // Sort rowSums and get the indices of the top 3 sums
        int[] indices = new int[3];
        for (int i = 0; i < 3; i++) {
            int maxIndex = 0;
            for (int j = 1; j < rowSums.length; j++) {
                if (rowSums[j] > rowSums[maxIndex]) {
                    maxIndex = j;
                }
            }
            indices[i] = maxIndex;
            rowSums[maxIndex] = Integer.MIN_VALUE; // Mark the maximum as processed
        }

        return indices;
    }

    // Find top three columns
    int[] findTopThreeColumns(int[][] array) {
        int[] colSums = new int[array[0].length];

        for (int i = 0; i < array[0].length; i++) {
            int sum = 0;
            for (int j = 0; j < array.length; j++) {
                sum += array[j][i];
            }
            colSums[i] = sum;
        }

        // Sort colSums and get the indices of the top 3 sums
        int[] indices = new int[3];
        for (int i = 0; i < 3; i++) {
            int maxIndex = 0;
            for (int j = 1; j < colSums.length; j++) {
                if (colSums[j] > colSums[maxIndex]) {
                    maxIndex = j;
                }
            }
            indices[i] = maxIndex;
            colSums[maxIndex] = Integer.MIN_VALUE; // Mark the maximum as processed
        }

        return indices;
    }
  
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
