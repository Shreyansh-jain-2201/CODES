#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
 
using namespace std;
 class students
 {
 private:
     int age,standard;
     string first_name,last_name;
 public:
    void setAge(int a)
    {
        age = a;
    }
    void set_standard(int a)
    {
        standard = a;
    }
    void set_first_name(string name)
    {
        first_name = name;
    }
    void set_last_name(string name)
    {
        last_name = name;
    }
    int getAge()
    {
        return age;
    }
    int getStandard()
    {
        return standard;
    }
    string get_first_name()
    {
        return first_name;
    }
    string get_last_name()
    {
        return last_name;
    }
    void GetDetails()
    {
        // string age = to_string(age);
        // string standard = to_string(standard);
        cout<<age<<","<<first_name<<","<<last_name<<","<<standard;
    }
 };
 
int main()
{
    int age,standard;
    students s;
    string fname,lname;
    cin>>age>>fname>>lname>>standard;
    s.setAge(age);
    s.set_first_name(fname);
    s.set_last_name(lname);
    s.set_standard(standard);
    cout<<s.getAge()<<endl;
    cout<<s.get_last_name()<<", "<<s.get_first_name()<<endl;
    cout<<s.getStandard()<<endl<<endl;
    s.GetDetails();
return 0;
}