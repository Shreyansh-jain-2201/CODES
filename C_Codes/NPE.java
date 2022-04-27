public class NPE
{
    public static void main(String args[])
    {
        try
        {
            String arr[] = new String[10];
            arr = null;
            arr[0] = "hello";
            System.out.println(arr[0]);
        }catch(Exception e)
        {
            System.out.println("Exception Arised");
        }
        catch(NullPointerException npe)
        {
            System.out.println("Null pointer exception");
        }
    }
}