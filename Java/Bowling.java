class Account implements Runnable {
    public static int balance = 0;
    synchronized public void deposite(int amount) {
        balance = balance + amount;
        System.out.println("Deposite: " + balance);
        notify();
    }
    synchronized public void withdraw(int amount) {
        if(balance >= amount) {
            balance = balance - amount;
            System.out.println("Withdraw: " + balance);
        }
        else {
            try {
                System.out.println("Waiting for balance to be available");
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
    @Override
    public void run() {
        // TODO Auto-generated method stub
        
    }
}

public class Bowling
{
    public static void main(String[] args) {
        Account account = new Account();
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                for (int i = 0; i < 10000; i++) {
                    account.deposite(1500);
                }
            }
        });
        Thread t2 = new Thread(new Runnable() {
            @Override
            public void run() {
                for (int i = 0; i < 10000; i++) {
                    account.withdraw(1500);
                }
            }
        });
        t1.start();
        t2.start();
        try {
            t1.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        try {
            t2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("Balance is " + account.balance);
    }
}