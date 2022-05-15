import java.util.Scanner;
import java.util.Arrays;

class Rectangle {
    private static double length, breadth;

    public static void set(double l, double b) {
        if (l > 0) {
            length = l;
        } else {
            length = 0;
        }
        if (b > 0) {
            breadth = b;
        } else {
            breadth = 0;
        }
    }

    public static double getLength() {
        return length;
    }

    public static double getBreadth() {
        return breadth;
    }

    public static double area() {
        return length * breadth;
    }

    public static double perimeter() {
        return 2 * (length + breadth);
    }
}

class practice {
    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {

            Rectangle R1 = new Rectangle();
            R1.set(3, 5);
            System.out.println(R1.getLength());
            System.out.println(R1.getBreadth());
            System.out.println(R1.area());
            System.out.println(R1.perimeter());
        }
    }
}
