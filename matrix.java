import java.util.Random;
import java.util.Scanner;

public class matrix {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[][] matrix = generateRandomMatrix(10, 10);

        for (String[] row : matrix) {
            for (String cell : row) {
                System.out.print(cell + " ");
            }
            System.out.println();
        }
        
        
        System.out.print("Enter a word to search in the matrix: ");
        String input = scanner.nextLine();
        
        searchWord(matrix, input);
        
        scanner.close();
    }

    public static String[][] generateRandomMatrix(int rows, int cols) {
        String[][] matrix = new String[rows][cols];
        Random random = new Random();
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                matrix[i][j] = String.valueOf((char) ('a' + random.nextInt(26)));
            }
        }
        return matrix;
    }

    public static void searchWord(String[][] matrix, String word) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        boolean found = false;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (j <= cols - word.length() && checkWord(matrix, word, i, j, 0, 1)) {
                    System.out.println("Found " + word + " at position: (" + i + ", " + j + ") horizontally.");
                    found = true;
                }
                if (i <= rows - word.length() && checkWord(matrix, word, i, j, 1, 0)) {
                    System.out.println("Found " + word + " at position: (" + i + ", " + j + ") vertically.");
                    found = true;
                }
            }
        }

        if (!found) {
            System.out.println("Word not found in the matrix.");
        }
    }

    public static boolean checkWord(String[][] matrix, String word, int row, int col, int fRow, int fCol) {
        for (int k = 0; k < word.length(); k++) {
            if (matrix[row + k * fRow][col + k * fCol].charAt(0) != word.charAt(k)) {
                return false;
            }
        }
        return true;
    }
}

