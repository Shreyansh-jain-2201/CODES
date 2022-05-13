// In a restaurant, Pastry Chef prepares sweet for their customers. The Chef makes sweet and stacks it up in a bowl, and the customers eats from it. The max capacity of the bowl is 20. If the bowl is empty, the Customer wait for the Chef to prepare new sweet. Use the Java programming language to demonstrate the given scenario using the concept of Inter Thread communication.

import java.util.Scanner;

class Chef implements Runnable {
    synchronized void preparePastry() {
        System.out.println("Chef is preparing pastry");
        notifyAll();
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void run() {
        while (true) {
            synchronized (this) {
                if (Bowl.isEmpty()) {
                    preparePastry();
                } else {
                    System.out.println("Chef is waiting for the bowl to be empty");
                    try {
                        wait();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        }
    }
}

class Customer implements Runnable {
    @Override
    public void run() {
        while (true) {
            synchronized (this) {
                if (Bowl.isEmpty()) {
                    System.out.println("Customer is waiting for the bowl to be filled");
                    try {
                        wait();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                } else {
                    System.out.println("Customer is eating");
                    try {
                        Thread.sleep(1000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    Bowl.emptyBowl();
                    notifyAll();
                }
            }
        }
    }
}

class Bowl {
    static boolean isEmpty = true;

    static void fillBowl() {
        isEmpty = false;
    }

    static void emptyBowl() {
        isEmpty = true;
    }

    static boolean isEmpty() {
        return isEmpty;
    }}
    public class ThreadDemo {

    public static void main(String[] args) {
        Chef chef = new Chef();
        Customer customer = new Customer();
        Thread t1 = new Thread(chef);
        Thread t2 = new Thread(customer);
        t1.start();
        t2.start();
    }
}

