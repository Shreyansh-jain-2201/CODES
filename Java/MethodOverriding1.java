class Bus

{

  void seatingCapacity()

  {

    System.out.println("Superclass Seats=32");

  }

}

class ElectricBus extends Bus

{

  void seatingCapacity()

  {

    System.out.println("Subclass Seats=20");

  }

  void showInfo()

  {

    seatingCapacity();

    this.seatingCapacity();

  }

}

public class MethodOverriding1

{

  public static void main(String[] args)

  {

    ElectricBus eb = new ElectricBus();

eb.showInfo();

 }

}