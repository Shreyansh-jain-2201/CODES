// Read the file "Holi.txt" and skip the first 11 characters and print rest of the information using the same class.
// Use RandomAccessFile
import java.io.*;

public class RandomAccessFileDemo {

  public static void main(String[] args) throws IOException {
    RandomAccessFile raf = new RandomAccessFile("Holi.txt", "r");
    raf.seek(11);
    String s = raf.readLine();
    System.out.println(s);
    raf.close();
  }
}
