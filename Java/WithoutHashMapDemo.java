import java.util.*;

public class WithoutHashMapDemo {

  public static void main(String[] args) {
    String str = "";
    // Copy commandline arguments to str
    for (int i = 0; i < args.length; i++) {
      str += args[i];
    }
    String alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ";
    List<List<Integer>> list = new ArrayList<List<Integer>>();
    List<Integer> list1 = new ArrayList<Integer>();
    for (int i = 0; i < alphabets.length(); i++) {
      list.add(new ArrayList<Integer>());
    }
    for (int i = 0; i < str.length(); i++) {
      int indexInAlphabets = alphabets.indexOf(str.charAt(i));
      list1 = list.get(indexInAlphabets);
      list1.add(i);
      list.set(indexInAlphabets, list1);
    }
    for (int i = 0; i < list.size(); i++) {
      if (list.get(i).size() > 0) {
        System.out.print(alphabets.charAt(i) + ": " + list.get(i) + " ");
      }
    }
  }
}
