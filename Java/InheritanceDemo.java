import java.util.Scanner;

// Suppose the weekly hours for all employees are stored in a two-dimensional array. Each row records an employee's seven-day work hours with seven columns. For example, the following array stores the work hours for eight employees. Write a Java program that displays employees and their total hours in decreasing order of the total hours.

// Su M T W Th F Sa

// Employee0 2 4 3 4 5 8 8

// Employee1 7 3 4 3 3 4 4

// Employee2 3 3 4 3 3 2 2

// Employee3 9 347 34 1

// Employee4 3 5 4 36 38

// Employee5 3 4 4 6 3 4 4

// Employee6 3 7 4 8 38 4

// Employee7 6 3 5 9 2 7 9

class Employee
{
    int empno;
    String name;
    int totalhours;
    int[][] hours;

    Employee(int empno, String name, int[][] hours)
    {
        this.empno = empno;
        this.name = name;
        this.hours = hours;
    }
}

public class InheritanceDemo {
    public static void main(String[] args) {
        int n;
        System.out.println("Enter the number of employees: ");
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        Employee[] emp = new Employee[n];
        for (int i = 0; i < n; i++) {
            System.out.println("Enter the details of employee " + (i + 1) + ": ");
            System.out.println("Enter the employee number: ");
            int empno = sc.nextInt();
            System.out.println("Enter the employee name: ");
            String name = sc.next();
            int[][] hours = new int[7][7];
            for (int j = 0; j < 7; j++) {
                for (int k = 0; k < 7; k++) {
                    System.out.println("Enter the hours for day " + (j + 1) + " and week " + (k + 1) + ": ");
                    hours[j][k] = sc.nextInt();
                }
            }
            emp[i] = new Employee(empno, name, hours);
        }
        int[] totalhours = new int[n];
        for (int i = 0; i < n; i++) {
            totalhours[i] = 0;
            for (int j = 0; j < 7; j++) {
                for (int k = 0; k < 7; k++) {
                    totalhours[i] += emp[i].hours[j][k];
                }
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (totalhours[i] < totalhours[j]) {
                    int temp = totalhours[i];
                    totalhours[i] = totalhours[j];
                    totalhours[j] = temp;
                    Employee tempemp = emp[i];
                    emp[i] = emp[j];
                    emp[j] = tempemp;
                }
            }
        }
        System.out.println("The employees and their total hours in decreasing order of the total hours are: ");
        for (int i = 0; i < n; i++) {
            System.out.println("Employee " + emp[i].empno + " " + emp[i].name + " " + totalhours[i]);
        }
        

    }
}