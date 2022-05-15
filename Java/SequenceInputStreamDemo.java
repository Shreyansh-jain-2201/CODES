// Write a java program to copy the content of two files (file1.txt, file2.txt) to a third
// file called file3.txt.
// Clue: SequenceInputStream
import java.io.*;

public class SequenceInputStreamDemo {

  public static void main(String[] args) throws IOException {
    File file1 = new File("file1.txt");
    File file2 = new File("file2.txt");
    File file3 = new File("file3.txt");
    FileInputStream fileInputStream1 = new FileInputStream(file1);
    FileInputStream fileInputStream2 = new FileInputStream(file2);
    SequenceInputStream sequenceInputStream = new SequenceInputStream(
      fileInputStream1,
      fileInputStream2
    );
    FileOutputStream fileOutputStream = new FileOutputStream(file3);
    int i;
    while ((i = sequenceInputStream.read()) != -1) {
      fileOutputStream.write(i);
    }
    fileOutputStream.close();
    sequenceInputStream.close();
    fileInputStream1.close();
    fileInputStream2.close();
  }
}
