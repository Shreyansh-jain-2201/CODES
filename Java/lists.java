import java.util.*;

public class lists {

  static List<Integer>[] add(List<Integer>[] list, int m, int x) {
    list[m].add(list[m].size(), x);
    return list;
  }

  static List<Integer>[] addFront(List<Integer> list[], int m, int x) {
    list[m].add(0, x);
    return list;
  }

  static List<Integer>[] delete(List<Integer> list[], int m, int k) {
    list[m].remove(list[m].get(k));
    return list;
  }

  static int diff(List<Integer> list1, List<Integer> list2) {
    HashSet<Integer> set1 = new HashSet<Integer>();
    HashSet<Integer> set2 = new HashSet<Integer>();
    for (int i = 0; i < list1.size(); i++) {
      set1.add(list1.get(i));
    }
    for (int i = 0; i < list2.size(); i++) {
      set2.add(list2.get(i));
    }
    // Find count of set1 and set2 and find the difference
    int count1 = set1.size();
    int count2 = set2.size();
    int diff = java.lang.Math.abs(count1 - count2);
    return diff;
  }

  static void printLists(List<Integer>[] list) {
    for (int i = 0; i < list.length; i++) {
      System.out.println(list[i]);
    }
  }

  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    System.out.println("Enter the number of lists: ");
    int n = input.nextInt();
    List<Integer>[] list = new List[n];
    for (int i = 0; i < n; i++) {
      list[i] = new ArrayList<Integer>();
    }
    System.out.println("Enter the number of elements in each list: ");
    int[] m = new int[n];
    for (int i = 0; i < n; i++) {
      m[i] = input.nextInt();
    }
    System.out.println("Enter the elements in each list: ");
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m[i]; j++) {
        list[i].add(input.nextInt());
      }
    }
    printLists(list);
    System.out.println("Enter the list number and the element to be added: ");
    int m1 = input.nextInt();
    int x = input.nextInt();
    list = add(list, m1, x);
    printLists(list);
    System.out.println(
      "Enter the list number and the element on to be added on the front: "
    );
    int m2 = input.nextInt();
    x = input.nextInt();
    list = addFront(list, m2, x);
    printLists(list);
    System.out.println("Enter the list number and the element to be deleted: ");
    int m3 = input.nextInt();
    int k = input.nextInt();
    list = delete(list, m3, k);
    printLists(list);
    System.out.println("Enter the first list number: ");
    int m4 = input.nextInt();
    System.out.println("Enter the second list number: ");
    int m5 = input.nextInt();
    System.out.println(
      "The difference between the counts of unique elements of two lists is: " +
      diff(list[m4], list[m5])
    );
    input.close();
  }
}
