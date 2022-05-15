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
import java.util.Scanner;

class InvalidCredentialsException extends Exception {

  public InvalidCredentialsException(String message) {
    super(message);
  }
}

class InvalidNameException extends InvalidCredentialsException {

  public InvalidNameException(String message) {
    super(message);
  }
}

class InvalidCountryException extends InvalidCredentialsException {

  public InvalidCountryException(String message) {
    super(message);
  }
}

class InvalidAgeException extends InvalidCredentialsException {

  public InvalidAgeException(String message) {
    super(message);
  }
}

class InvalidContactException extends InvalidCredentialsException {

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

  public String getName() {
    return name;
  }

  public int getAge() {
    return age;
  }

  public String getPhone() {
    return phone;
  }

  public String getCountry() {
    return country;
  }

  void checkName() throws InvalidNameException {
    char c[] = name.toCharArray();
    for (char i : c) {
      if (Character.isDigit(i)) {
        throw new InvalidNameException("Invalid Name");
      }
    }
  }

  void checkAge() throws InvalidAgeException {
    if (this.age < 18) {
      throw new InvalidAgeException("Invalid Age");
    }
  }

  void checkPhone() throws InvalidContactException {
    if (this.phone.length() != 10) {
      throw new InvalidContactException("Invalid Contact");
    }
  }

  void checkCountry() throws InvalidCountryException {
    if (!this.country.equals("India")) {
      throw new InvalidCountryException("Invalid Country");
    }
  }
}

public class VotersDetails {

  public static void main(String[] args) {
    Voter[] voter = new Voter[2];
    String name, phone, country;
    int age;
    try {
      DataInputStream in = new DataInputStream(System.in);
      BufferedReader br = new BufferedReader(new InputStreamReader(in));
      Scanner input = new Scanner(System.in);
      for (int i = 0; i < 2; i++) {
        System.out.print("Enter the name: ");
        name = br.readLine();
        System.out.print("Enter the age: ");
        age = Integer.parseInt(br.readLine());
        System.out.print("Enter the phone number: ");
        phone = br.readLine();
        System.out.print("Enter the country: ");
        country = br.readLine();
        voter[i] = new Voter(name, age, phone, country);
        int j = 0;
        try {
          voter[i].checkName();
          j++;
        } catch (InvalidNameException e) {
          System.out.println(e.getMessage());
        }
        try {
          voter[i].checkAge();
          j++;
        } catch (InvalidAgeException e) {
          System.out.println(e.getMessage());
        }
        try {
          voter[i].checkPhone();
          j++;
        } catch (InvalidContactException e) {
          System.out.println(e.getMessage());
        }
        try {
          voter[i].checkCountry();
          j++;
        } catch (InvalidCountryException e) {
          System.out.println(e.getMessage());
        }
        if (j == 4) {
          System.out.println("The voter is eligible to cast his vote");
        } else {
          System.out.println("The voter is not eligible to cast his vote");
        }
      }
      br.close();
      in.close();
      input.close();
    } catch (IOException e) {
      System.out.println(e.getMessage());
    } catch (Exception ex) {
      System.out.println(ex.getMessage());
    }
  }
}
