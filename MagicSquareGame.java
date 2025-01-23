import java.util.Random;
import java.util.Scanner;

public class MagicSquareGame {
    private static int[][] magicSquare;
    private static int n;
    private static int moves;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter an odd integer for the size of the magic square: ");
        n = scanner.nextInt();
    
        if (n % 2 == 0) {
            System.out.println("Please enter an odd integer.");
            scanner.close();
            return;
        }
    
        initializeMagicSquare();
        shuffleMagicSquare();
        displayMagicSquare();
        
        moves = 0;
        Scanner moveScanner = new Scanner(System.in); // Initialize moveScanner outside the loop
        while (!isMagicSquare()) {
            System.out.println("Enter a move (i j direction):");
            while (!moveScanner.hasNextInt()) { // Check if there's an integer available
                System.out.println("Invalid input. Enter a move (i j direction):");
                moveScanner.next(); // Clear the invalid input
            }
            int i = moveScanner.nextInt() - 1; // Adjust indices to start from 0
            int j = moveScanner.nextInt() - 1;
            
            if (i < 0 || i >= n || j < 0 || j >= n) { // Check if position is out of bounds
                System.out.println("Invalid position. Position must be within the magic square.");
                continue; // Prompt the user again for valid input
            }
            
            // Check if there's a char available (direction input)
            while (!moveScanner.hasNext()) {
                System.out.println("Invalid input. Enter a move (i j direction):");
                moveScanner.nextLine(); // Clear the invalid input
            }
            char direction = moveScanner.next().charAt(0);
            
            makeMove(i, j, direction);
            moves++;
            displayMagicSquare();
        }
    
        moveScanner.close(); // Close moveScanner after the game is completed
        scanner.close(); // Close scanner after the game is completed
    
        System.out.println("Congratulations! You completed the magic square in " + moves + " moves.");
    }

    private static void initializeMagicSquare() {
        magicSquare = new int[n][n];
        int x = 0;
        int y = n / 2;

        for (int i = 1; i <= n * n; i++) {
            magicSquare[x][y] = i;

            int newX = (x - 1 + n) % n;
            int newY = (y + 1) % n;

            if (magicSquare[newX][newY] == 0) {
                x = newX;
                y = newY;
            } else {
                x = (x + 1) % n;
            }
        }
    }

    private static void shuffleMagicSquare() {
        Random random = new Random();
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    int newX = i;
                    int newY = j;
                    while ((newX == i && newY == j) || (Math.abs(newX - i) + Math.abs(newY - j) != 1)) {
                        int direction = random.nextInt(4);
                        switch (direction) {
                            case 0: // Up
                                newX = (i - 1 + n) % n;
                                newY = j;
                                break;
                            case 1: // Down
                                newX = (i + 1) % n;
                                newY = j;
                                break;
                            case 2: // Left
                                newX = i;
                                newY = (j - 1 + n) % n;
                                break;
                            case 3: // Right
                                newX = i;
                                newY = (j + 1) % n;
                                break;
                        }
                    }
                    int temp = magicSquare[i][j];
                    magicSquare[i][j] = magicSquare[newX][newY];
                    magicSquare[newX][newY] = temp;
                }
            }
        }
    }

    private static boolean isMagicSquare() {
        int targetSum = n * (n * n + 1) / 2;
        int sum = 0;

        // Check rows and columns
        for (int i = 0; i < n; i++) {
            int rowSum = 0;
            int colSum = 0;
            for (int j = 0; j < n; j++) {
                rowSum += magicSquare[i][j];
                colSum += magicSquare[j][i];
            }
            if (rowSum != targetSum || colSum != targetSum) {
                return false;
            }
        }

        // Check diagonals
        int diagSum1 = 0;
        int diagSum2 = 0;
        for (int i = 0; i < n; i++) {
            diagSum1 += magicSquare[i][i];
            diagSum2 += magicSquare[i][n - 1 - i];
        }
        if (diagSum1 != targetSum || diagSum2 != targetSum) {
            return false;
        }

        return true;
    }

    private static void makeMove(int i, int j, char direction) {
        int newX = i, newY = j;
        switch (direction) {
            case 'U':
                newX = (i - 1 + n) % n;
                break;
            case 'D':
                newX = (i + 1) % n;
                break;
            case 'L':
                newY = (j - 1 + n) % n;
                break;
            case 'R':
                newY = (j + 1) % n;
                break;
            default:
                System.out.println("Invalid direction.");
                return;
        }
    
        int temp = magicSquare[i][j];
        magicSquare[i][j] = magicSquare[newX][newY];
        magicSquare[newX][newY] = temp;
    }
    
   

    private static void displayMagicSquare() {
        System.out.println("Magic Square:");
        for (int[] row : magicSquare) {
            for (int num : row) {
                System.out.print(num + " ");
            }
            System.out.println();
        }
    }
}
