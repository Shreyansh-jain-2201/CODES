// Assume that a customer requires to login into SELFCARE APP using a typical login credential information such as username and password. To create a user and his/her password, the app checks the validity of password supplied by the user using the following constraint.

// a. Minimum password length of 8 b. At least one uppercase letter in password

// c. At least one symbol in the set (*, S, #, !) is present Create an Exception with name LoginException that will be raised whenever the password supplied is not matched with the above constraint. Implement a method checkPass(String pass) that will assign the responsibility to handle the above exception by its caller. If the password is valid, then show a captcha generated using the random number generator method as a two digit random number to the user and ask the user to enter the same captcha. With inner try block, check the validity of the captcha and then throw the same exception with different exception message. Test the validity of the password and captcha using main method of your driver program.

// Note: int rand = (int) (Math.random()* 10)+1 // generate

// random numbers within 1 to 10.

import java.util.Scanner;

class LoginException extends Exception {
    public LoginException(String message) {
        super(message);
    }
}


public class ExceptionDemo {
    static void checkPass(String pass) throws LoginException {
        boolean lengthIsValid = false;
        boolean upperCaseIsValid = false;
        boolean symbolIsValid = false;

        int n = pass.length();
        if (n >= 8) {
            lengthIsValid = true;
        }
        for (int i = 0; i < n; i++) {
            if (Character.isUpperCase(pass.charAt(i))) {
                upperCaseIsValid = true;
            }
        }
        for (int i = 0; i < n; i++) {
            if (pass.charAt(i) == '*' || pass.charAt(i) == 'S' || pass.charAt(i) == '#' || pass.charAt(i) == '!') {
                symbolIsValid = true;
            }
        }
        if (!lengthIsValid) {
            throw new LoginException("Password length is not valid!");
        }
        else if(!upperCaseIsValid)
        {
            throw new LoginException("Password does not contain at least one uppercase letter!");
        }
        else if(!symbolIsValid)
        {
            throw new LoginException("Password does not contain at least one symbol!");
        }
        else
        {
            System.out.println("Password is valid!");
        }
        

    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter password");
        String pass = scan.nextLine();
        try {
            checkPass(pass);
        } catch (LoginException e) {
            System.out.println(e.getMessage());
        }
        scan.close();
    }
}

