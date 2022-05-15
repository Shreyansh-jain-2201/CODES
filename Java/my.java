import java.util.*;

class my {
    public static void main(String[] args) {
        try (Scanner s = new Scanner(System.in)) {
            int a, b, c;
            a = s.nextInt();
            b = s.nextInt();
            c = a + b;
            System.out.println(c);
        }
    }
}