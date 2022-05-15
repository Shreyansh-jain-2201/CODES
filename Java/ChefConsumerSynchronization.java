// Consider you want to eat a set of items in an order at famous Vellore Barbeque
// Nation (V-BBQ). The sequence includes juice, soup, chicken tikka, kabab, paneer
// tikka, fish65, biriyani rice, lime juice, butter milk, fruit salad, and pan. The same
// sequence has been updated to the server who serves the food on your plate. He can
// serve the food in an order mentioned by the client. Create a Server and Customer
// problem in Threads using Thread Synchronization for the above mentioned
// scenario. The graphical representation of the scenario is given below.

// Producer -> Notification: Food is ready -> Consumer
// Consumer -> Notification: Food is eaten -> Producer
// Producer, consumer -> Condition variables

import java.util.*;

public class ChefConsumerSynchronization {

  public static class Plate {
    private String item;
    private boolean empty = true;

    public synchronized void put(String item) {
      while (!empty) {
        try {
          wait();
        } catch (InterruptedException e) {
          System.out.println("Interrupted");
        }
      }
      this.item = item;
      empty = false;
      notifyAll();
    }

    public synchronized String take() {
      while (empty) {
        try {
          wait();
        } catch (InterruptedException e) {
          System.out.println("Interrupted");
        }
      }
      empty = true;

      notifyAll();
      return this.item;
    }
  }
}

public static class Server implements Runnable {
  private Plate plate;

  public Server(Plate plate) {
    this.plate = plate;
  }

  public void run() {
    String items[] = {
      "Juice",
      "Soup",
      "Chicken Tikka",
      "Kabab",
      "Paneer Tikka",
      "Fish65",
      "Biriyani Rice",
      "Lime Juice",
      "Butter Milk",
      "Fruit Salad",
      "Pan",
    };
    Random random = new Random();
    for (int i = 0; i < items.length; i++) {
      plate.put(items[i]);
      try {
        Thread.sleep(random.nextInt(5000));
      } catch (InterruptedException e) {
        System.out.println("Interrupted");
      }
    }
    plate.put("DONE");
  }
}

public static class Customer implements Runnable {
  private Plate plate;

  public Customer(Plate plate) {
    this.plate = plate;
  }

  public void run() {
    Random random = new Random();
    for (
      String message = plate.take();
      !message.equals("DONE");
      message = plate.take()
    ) {
      System.out.println("Customer is eating " + message);
      try {
        Thread.sleep(random.nextInt(5000));
      } catch (InterruptedException e) {
        System.out.println("Interrupted");
      }
    }
  }
}
