// Write a Java Program that provides that following options for an user
// 1. Gets the details of a car object (carId,ModelName,BrandName,Price) from the user and inserts the data in the CAR table on the MySQL Database
// 2. Updates the ModelName for any carId in the database by getting the modelname and carid from the user
// 3. Displays the CarId,BrandName and Price from the database for a ModelName entered by the user.
// 4. The user can view the Average price for each Brand from the database.
// 5. The user can delete any record using part of the ModelName. If the user enters SWI then all cars which contain SWI as part of the Model Name will be deleted from the database 

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.Scanner;

public class jdbcDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int choice = 0;
        do {
            System.out.println("1. Insert");
            System.out.println("2. Update");
            System.out.println("3. Display");
            System.out.println("4. Average");
            System.out.println("5. Delete");
            System.out.println("6. Exit");
            System.out.println("Enter your choice");
            choice = sc.nextInt();
            switch (choice) {
            case 1:
                insert();
                break;
            case 2:
                update();
                break;
            case 3:
                display();
                break;
            case 4:
                average();
                break;
            case 5:
                delete();
                break;
            case 6:
                System.out.println("Thank you");
                break;
            default:
                System.out.println("Invalid choice");
                break;
            }
        } while (choice != 6);
    }

    public static void insert() {
        Scanner sc = new Scanner(System.in);
        Connection con = null;
        PreparedStatement pstmt = null;
        try {
            Class.forName("com.mysql.jdbc.Driver");
            con = DriverManager.getConnection("jdbc:mysql://localhost:3306/jdbc", "root", "root");
            System.out.println("Enter the carId");
            int carId = sc.nextInt();
            System.out.println("Enter the ModelName");
            String modelName = sc.next();
            System.out.println("Enter the BrandName");
            String brandName = sc.next();
            System.out.println("Enter the Price");
            int price = sc.nextInt();
            pstmt = con.prepareStatement("insert into car values(?,?,?,?)");
            pstmt.setInt(1, carId);
            pstmt.setString(2, modelName);
            pstmt.setString(3, brandName);
            pstmt.setInt(4, price);
            int count = pstmt.executeUpdate();
            if (count > 0) {
                System.out.println("Record inserted");
            } else {
                System.out.println("Record not inserted");
            }
        } catch (Exception e) {
            System.out.println(e);
        } finally {
            try {
                pstmt.close();
                con.close();
            } catch (Exception e) {
                System.out.println(e);
            }
        }
    }
    public static void update() {
        Scanner sc = new Scanner(System.in);
        Connection con = null;
        PreparedStatement pstmt = null;
        try {
            Class.forName("com.mysql.jdbc.Driver");
            con = DriverManager.getConnection("jdbc:mysql://localhost:3306/jdbc", "root", "root");
            System.out.println("Enter the ModelName");
            String modelName = sc.next();
            System.out.println("Enter the carId");
            int carId = sc.nextInt();
            pstmt = con.prepareStatement("update car set ModelName=? where carId=?");
            pstmt.setString(1, modelName);
            pstmt.setInt(2, carId);
            int count = pstmt.executeUpdate();
            if (count > 0) {
                System.out.println("Record updated");
            } else {
                System.out.println("Record not updated");
            }
        } catch (Exception e) {
            System.out.println(e);
        } finally {
            try {
                pstmt.close();
                con.close();
            } catch (Exception e) {
                System.out.println(e);
            }
        }
    }

    public static void display() {
        Scanner sc = new Scanner(System.in);
        Connection con = null;
        PreparedStatement pstmt = null;
        try {
            Class.forName("com.mysql.jdbc.Driver");
            con = DriverManager.getConnection("jdbc:mysql://localhost:3306/jdbc", "root", "root");
            System.out.println("Enter the ModelName");
            String modelName = sc.next();
            pstmt = con.prepareStatement("select * from car where ModelName=?");
            pstmt.setString(1, modelName);
            ResultSet rs = pstmt.executeQuery();
            while (rs.next()) {
                System.out.println("CarId:" + rs.getInt(1));
                System.out.println("ModelName:" + rs.getString(2));
                System.out.println("BrandName:" + rs.getString(3));
                System.out.println("Price:" + rs.getInt(4));
            }
        } catch (Exception e) {
            System.out.println(e);
        } finally {
            try {
                pstmt.close();
                con.close();
            } catch (Exception e) {
                System.out.println(e);
            }
        }
    }
    public static void average() {
        Scanner sc = new Scanner(System.in);
        Connection con = null;
        PreparedStatement pstmt = null;
        try {
            Class.forName("com.mysql.jdbc.Driver");
            con = DriverManager.getConnection("jdbc:mysql://localhost:3306/jdbc", "root", "root");
            System.out.println("Enter the BrandName");
            String brandName = sc.next();
            pstmt = con.prepareStatement("select avg(Price) from car where BrandName=?");
            pstmt.setString(1, brandName);
            ResultSet rs = pstmt.executeQuery();
            while (rs.next()) {
                System.out.println("Average Price:" + rs.getInt(1));
            }
        } catch (Exception e) {
            System.out.println(e);
        } finally {
            try {
                pstmt.close();
                con.close();
            } catch (Exception e) {
                System.out.println(e);
            }
        }
    }

    public static void delete() {
        Scanner sc = new Scanner(System.in);
        Connection con = null;
        PreparedStatement pstmt = null;
        try {
            Class.forName("com.mysql.jdbc.Driver");
            con = DriverManager.getConnection("jdbc:mysql://localhost:3306/jdbc", "root", "root");
            System.out.println("Enter the carId");
            int carId = sc.nextInt();
            pstmt = con.prepareStatement("delete from car where carId=?");
            pstmt.setInt(1, carId);
            int count = pstmt.executeUpdate();
            if (count > 0) {
                System.out.println("Record deleted");
            } else {
                System.out.println("Record not deleted");
            }
        } catch (Exception e) {
            System.out.println(e);
        } finally {
            try {
                pstmt.close();
                con.close();
            } catch (Exception e) {
                System.out.println(e);
            }
        }
    }
}