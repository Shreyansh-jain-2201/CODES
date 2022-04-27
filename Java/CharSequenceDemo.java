// Write a class that implements the CharSequence interface found in the java.lang package.
// Your implementation should return the string backwards.

import java.lang.CharSequence;

import java.util.*;

class Sequence implements CharSequence {
  public Sequence(String s) {
    this.s = s;
  }
    public char charAt(int index) {
    return s.charAt(s.length() - index - 1);
  }
  public int length() {
    return s.length();
  }
  public Sequence subSequence(int start, int end) {
    return new Sequence(s.substring(start, end));
  }
    public String toString() {
        return s;
    }
    public void reverse() {
        StringBuilder sb = new StringBuilder();
        for (int i = s.length() - 1; i >= 0; i--) {
            sb.append(s.charAt(i));
        }
        s = sb.toString();
    }
  private String s;
}

public class CharSequenceDemo {
  public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
        System.out.println("Enter a string: ");
        String s = scan.nextLine();
        Sequence seq = new Sequence(s);
        System.out.println("The string is: " + seq);
        seq.reverse();
        System.out.println("The reversed string is: " + seq);
    }
}