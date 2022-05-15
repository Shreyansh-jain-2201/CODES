import java.util.*;

public class HashMapDemo {

  public static void main(String[] args) {
    // Take input as command-line arguments
    String str = "";
    // Copy commandline arguments to str
    for (int i = 0; i < args.length; i++) {
      str += args[i];
    }
    HashMap<Character, List<Integer>> map = new HashMap<Character, List<Integer>>();
    for (int i = 0; i < str.length(); i++) {
      char ch = str.charAt(i);
      if (ch != ' ') {
        if (map.containsKey(ch)) {
          map.get(ch).add(i);
        } else {
          List<Integer> list = new ArrayList<Integer>();
          list.add(i);
          map.put(ch, list);
        }
      }
    }
    System.out.println(map);
  }
}
