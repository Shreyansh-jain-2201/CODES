class Student {
  int marks[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
  int count[] = { 3, 4, 16, 9, 11, 8, 4, 6, 5, 2 };
  int fiXi = 0;
  int fi = 0;

  void setFiXi() {
    for (int i = 0; i < 10; i++) {
      this.fiXi += (count[i] * marks[i]);
    }
  }

  void setFi() {
    for (int i = 0; i < 10; i++) {
      this.fi += (count[i]);
    }
  }
}

public class ThreadDemo {

  public static void main(String[] args) {
    Student Shruti = new Student();
    Thread t1 = new Thread(
      new Runnable() {

        public void run() {
          Shruti.setFiXi();
        }
      }
    );
    Thread t2 = new Thread(
      new Runnable() {

        public void run() {
          Shruti.setFi();
        }
      }
    );
    t1.start();
    t2.start();
    try {
      t1.join();
    } catch (InterruptedException e1) {
      // TODO Auto-generated catch block
      e1.printStackTrace();
    }
    try {
      t2.join();
    } catch (InterruptedException e) {
      // TODO Auto-generated catch block
      e.printStackTrace();
    }
    System.out.println(Shruti.fiXi / Shruti.fi);
  }
}
