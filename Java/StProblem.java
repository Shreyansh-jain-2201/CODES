import java.util.Scanner;
import java.util.Arrays;

class  {
    static double sum(double ...x)
    {
        double s = 0.0;
        int n = x.length;
        for(double a:x)
        {
            s = s + a;
        }
        return discount(s);
    }
    static double discount(double s)
    {
        if(s<500)
        {
            return s/0.9;
        }
        return s/0.8;
    }
    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
           

        }
    }
}