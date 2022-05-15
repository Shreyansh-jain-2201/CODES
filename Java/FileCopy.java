// Write a program to copy the contents of more than two files into a single file.
// Clue: SequenceInputStream

import java.io.*;

public class FileCopy {

  public static void main(String[] args) throws IOException {
    File file1 = new File("file1.txt");
    File file2 = new File("file2.txt");
    File file3 = new File("file3.txt");
    File file4 = new File("file4.txt");
    File finalFile = new File("finalFile.txt");
    File files[] = { file1, file2, file3, file4, finalFile };
    for (int i = 0; i < files.length - 1; i++) {
      FileInputStream fileInputStream1 = new FileInputStream(files[i]);
      FileInputStream fileInputStream2 = new FileInputStream(files[i + 1]);
      SequenceInputStream sequenceInputStream = new SequenceInputStream(
        fileInputStream1,
        fileInputStream2
      );
      FileOutputStream fileOutputStream = new FileOutputStream(files[i + 1]);
      int i1;
      while ((i1 = sequenceInputStream.read()) != -1) {
        fileOutputStream.write(i1);
      }
      fileOutputStream.close();
      sequenceInputStream.close();
      fileInputStream1.close();
      fileInputStream2.close();
    }
    // Print the contents of the finalFile
    FileInputStream fileInputStream = new FileInputStream(finalFile);
    int i;
    while ((i = fileInputStream.read()) != -1) {
      System.out.print((char) i);
    }
    fileInputStream.close();
  }
}
