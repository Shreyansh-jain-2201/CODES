// A person in our country is eligible to cast their vote if the one satisfies two
// conditions. (i) The person must be an Indian, (ii) must have at least 18 years. If the
// Government has assigned a task to maintain the database of our Indian voters list.
// In this regard, you started collecting the information of each person if the one is
// eligible. Collect the information for the following attributes: name, age, phone
// number, and country of residence. Generate the following exceptions when the
// information entered by user is wrong.
// a. Throw InvalidNameException if the entered name is having any numerals.
// b. Throw InvalidAgeException if the age is <18
// c. Throw InvalidContactException if the mobile number is more than 10
// digits.
// d. Throw InvalidCountryException if the country of residence is not India.
// Use the combination of DataInputStream and BufferedReader classes to read
// the input from keyboard. Give some differences between them.

import java.io.*;

class InvalidNameException extends Exception {

  public InvalidNameException(String message) {
    super(message);
  }
}

class InvalidCountryException extends Exception {

  public InvalidCountryException(String message) {
    super(message);
  }
}

class InvalidAgeException extends Exception {

  public InvalidAgeException(String message) {
    super(message);
  }
}

class InvalidContactException extends Exception {

  public InvalidContactException(String message) {
    super(message);
  }
}

class Voter {
  String name;
  int age;
  String phone;
  String country;

  public Voter(String name, int age, String phone, String country) {
    this.name = name;
    this.age = age;
    this.phone = phone;
    this.country = country;
  }

  public void validate()
    throws InvalidNameException, InvalidAgeException, InvalidContactException, InvalidCountryException {
    char c[] = name.toCharArray();
    for (char i : c) {
      if (Character.isDigit(i)) {
        throw new InvalidNameException("Invalid Name");
      }
    }
    if (age < 18) {
      throw new InvalidAgeException("Invalid Age");
    }
    if (phone.length() > 10) {
      throw new InvalidContactException("Invalid Contact");
    }
    if (!country.equals("India")) {
      throw new InvalidCountryException("Invalid Country");
    } else {
      System.out.println("Voter is eligible to cast their vote");
    }
  }
}

public class ValidVoter {

  public static void main(String[] args)
    throws InvalidNameException, InvalidAgeException, InvalidContactException, InvalidCountryException {
    try {
      DataInputStream in = new DataInputStream(System.in);
      BufferedReader reader = new BufferedReader(new InputStreamReader(in));
      String name, phone, country;
      int age;
      Voter[] voter = new Voter[3];
      for (int i = 0; i < 3; i++) {
        System.out.print("Enter the name of the voter: ");
        name = reader.readLine();
        System.out.print("Enter the age of the voter: ");
        age = Integer.parseInt(reader.readLine());
        System.out.print("Enter the phone number of the voter: ");
        phone = reader.readLine();
        System.out.print("Enter the country of the voter: ");
        country = reader.readLine();
        voter[i] = new Voter(name, age, phone, country);
        try {
          voter[i].validate();
        } catch (InvalidNameException e) {
          System.out.println(e.getMessage());
        } catch (InvalidAgeException e) {
          System.out.println(e.getMessage());
        } catch (InvalidContactException e) {
          System.out.println(e.getMessage());
        } catch (InvalidCountryException e) {
          System.out.println(e.getMessage());
        }
      }
    } catch (IOException e) {
      System.out.println(e.getMessage());
    }
  }
}
