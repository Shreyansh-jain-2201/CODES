// Write a Java program to implement the following: 

// a. Create a class DataStructure with members Size as integer and Values as array of integers of the "size". 
// b. Create a constructor to initialize the Size and size of the Values. 
// c. Create a signatures void Insert(int) and int Delete().
// d. Create another classes Stack and Queue which inherits DataStructure class.
// e. Stack has the member top and Queue has first and last as members. 
// f. Override Insert()and Delete() according to the process of Stack and Queue. 
// g. Create boolean isFull() and Boolean isEmpty() in both Stack and Queue classes.
// h. Create a void Traverse() method in both Stack and Queue to show the content. 1. Create a Demo class to demonstrate all above processes and show the content. after each process.

import java.util.Scanner;

class DataStructure {
    int size;
    int[] values;

    DataStructure(int size) {
        this.size = size;
        values = new int[size];
    }

    void insert(int value) {
        for (int i = 0; i < size; i++) {
            if (values[i] == 0) {
                values[i] = value;
                break;
            }
        }
    }

    int delete() {
        int value = 0;
        for (int i = 0; i < size; i++) {
            if (values[i] != 0) {
                value = values[i];
                values[i] = 0;
                break;
            }
        }
        return value;
    }
}

class Stack extends DataStructure {
    int top;

    Stack(int size) {
        super(size);
        top = -1;
    }

    void insert(int value) {
        if (top == size - 1) {
            System.out.println("Stack is full");
        } else {
            top++;
            super.insert(value);
        }
    }

    int delete() {
        if (top == -1) {
            System.out.println("Stack is empty");
            return 0;
        } else {
            top--;
            return super.delete();
        }
    }
}

class Queue extends DataStructure {
    int first;
    int last;

    Queue(int size) {
        super(size);
        first = -1;
        last = -1;
    }

    void insert(int value) {
        if (first == -1) {
            first = 0;
            last = 0;
        } else if (last == size - 1) {
            System.out.println("Queue is full");
        } else {
            last++;
        }
        super.insert(value);
    }

    int delete() {
        if (first == -1) {
            System.out.println("Queue is empty");
            return 0;
        } else if (first == last) {
            first = -1;
            last = -1;
        } else {
            first++;
        }
        return super.delete();
    }
}

public class n{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of stack");
        int size = sc.nextInt();
        Stack stack = new Stack(size);
        System.out.println("Enter the size of queue");
        int size1 = sc.nextInt();
        Queue queue = new Queue(size1);
        System.out.println("Enter the number of elements");
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            System.out.println("Enter the choice");
            System.out.println("1. Insert in stack");
            System.out.println("2. Insert in queue");
            System.out.println("3. Delete from stack");
            System.out.println("4. Delete from queue");
            System.out.println("5. Traverse stack");
            System.out.println("6. Traverse queue");
            int choice = sc.nextInt();
            switch (choice) {
                case 1:
                    System.out.println("Enter the value");
                    int value = sc.nextInt();
                    stack.insert(value);
                    break;
                case 2:
                    System.out.println("Enter the value");
                    int value1 = sc.nextInt();
                    queue.insert(value1);
                    break;
                case 3:
                    System.out.println("Deleted value is " + stack.delete());
                    break;
                case 4:
                    System.out.println("Deleted value is " + queue.delete());
                    break;
                case 5:
                    System.out.println("Stack is");
                    
                    break;
                case 6:
                    System.out.println("Queue is");
                    
                    break;
                default:
                    System.out.println("Invalid choice");
            }
        }
    }
}