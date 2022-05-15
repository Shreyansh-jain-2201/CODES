// Suppose if you want to write a code that write from a file one word at a time. The
// code needs to peek ahead to find where the words are separated by whitespace.
// What input stream could you use to accomplish this? Also give clue to read blocks
// of n-bytes from the file.
import java.io.*;
import java.util.*;

public class DataInputStreamDemo {

  public static void main(String[] args) throws IOException {
    File file = new File("words.txt");
    Scanner scanner = new Scanner(file);
    while (scanner.hasNext()) {
      String word = scanner.next();
      System.out.println(word);
    }
    scanner.close();
  }
}
