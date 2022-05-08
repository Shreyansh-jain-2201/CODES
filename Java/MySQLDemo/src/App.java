import java.sql.*;

public class App{
    public static void main(String args[]) throws InstantiationException, IllegalAccessException, ClassNotFoundException
    {
        try{
            Connection con = null;
            Class.forName("com.mysql.cj.jdbc.Driver").newInstance();
            con = DriverManager.getConnection("jdbc:mysql://localhost:3306/user", "Shreyansh", "root");
            System.out.println("Connection Succesfull");
        }
        catch(SQLException s)
        {
            System.out.println(s.getMessage());
        }
    }

}