import java.util.Scanner;

class mail {
    public static void main(String[] args) {
        try (Scanner s = new Scanner(System.in)) {
            int n = s.nextInt();
            for (int i = n; i >= 1; i--) {
                int p = n - i;
                for (int j = 1; j <= p; j++) {
                    System.out.print("  ");
                }
                for (int j = 1; j <= i; j++) {
                    System.out.print("* ");
                }
                System.out.println();
            }

        }
    }
}