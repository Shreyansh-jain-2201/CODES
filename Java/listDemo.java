/*Create n lists with different values in each list. Implement the following methods on the n list
add(m, x) - add the element x to the mth list
addFrom(m,x) - add the element x to the 0th position of the mth list
delete(m, k) - delete the kth element of the mth list
diff(m1, m2) - Finds the absolute difference between the unique elements of two lists*/

import java.util.*;

public class listDemo {

  static List<Integer> add(List<Integer> list, int m, int x) {
    list.add(m, x);
    return list;
  }

  static List<Integer> addFrom(List<Integer> list, int m, int x) {
    list.add(0, x);
    return list;
  }

  static List<Integer> delete(List<Integer> list[], int m, int k) {
    list[m].remove(list[m].get(list[k]));
  }

  static List<Integer> diff(List<Integer> list1, List<Integer> list2) {
    List<Integer> list3 = new ArrayList<Integer>();
    for (int i = 0; i < list1.size(); i++) {
      list3.add(java.lang.Math.abs((list1.get(i) - list2.get(i))));
    }
    return list3;
  }

  public static void main(String[] args) {
    List<Integer> list[] = new ArrayList[n];
    Scanner scan = new Scanner(System.in);
    int n = scan.nextInt();
    for (int i = 0; i < n; i++) {
      list[i] = new ArrayList<Integer>();
    }
    // Add elements to n lists
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        list[i].add(scan.nextInt());
      }
    }

    int m = scan.nextInt();
    int x = scan.nextInt();
    int k = scan.nextInt();
    int m1 = scan.nextInt();
    int m2 = scan.nextInt();
    for (int i = 0; i < n; i++) {
      System.out.println(add(list[i], m, x));
      System.out.println(addFrom(list[i], m, x));
      System.out.println(delete(list[i], m, k));
      System.out.println(diff(list[i], list[k]));
    }
  }
}
