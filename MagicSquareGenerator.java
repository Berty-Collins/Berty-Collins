import java.util.Scanner;

public class MagicSquareGenerator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter an odd integer for the size of the magic square: ");
        int n = scanner.nextInt();
        scanner.close();
        
        if (n % 2 == 0) {
            System.out.println("Please enter an odd integer.");
            return;
        }
        
        int[][] magicSquare = generateMagicSquare(n);
        displayMagicSquare(magicSquare);
    }

    private static int[][] generateMagicSquare(int n) {
        int[][] square = new int[n][n];
        int x = 0;
        int y = n / 2;
        
        for (int i = 1; i <= n * n; i++) {
            square[x][y] = i;
            
            int newX = (x - 1 + n) % n;
            int newY = (y - 1 + n) % n;
            
            if (square[newX][newY] == 0) {
                x = newX;
                y = newY;
            } else {
                x = (x + 1) % n;
            }
        }
        
        return square;
    }

    private static void displayMagicSquare(int[][] magicSquare) {
        System.out.println("Magic Square:");
        for (int[] row : magicSquare) {
            for (int num : row) {
                System.out.print(num + " ");
            }
            System.out.println();
        }
    }
}
