// #include <iostream>
// #include <cmath>
// #include <vector>
 
// using namespace std;

// class Fraction
// {
// private:
// int denominator;
// int gcd()
// {
//     int a = this->numerator;
//     int b = this->denominator;
//     int num = min(a,b);
//     for (int i = num; i>0; i--)
//     {
//         if (a%i == 0 && b%i == 0)
//         {
//             return i;
//         }
//     }
//     return 1;
// }
// public:
// int numerator;
// // Fraction(int numerator, int denominator)
// // {
// //     this->numerator = numerator;
// //     this->denominator = denominator;
// // }
// int getNumerator()
// {
//     return numerator;
// }
// // void setNumerator(int num)
// // {
// //     numerator = num;
// // }
// void simplify()
// {
//     int g = gcd();
//     this->numerator = this->numerator/g;
//     this->denominator = this->denominator/g;
// }
// void display()
// {
//     simplify();
//     cout << this->numerator<<"/"<<this->denominator;
// }

// void operator+ (Fraction f2)
// {
//     this->numerator = this->numerator*f2.denominator + this->denominator*f2.numerator;
//     this->denominator = this->denominator * f2.denominator;
//     display();
// }
// void operator* (Fraction f2)
// {
//     this->numerator = this->numerator*f2.numerator;
//     this->denominator = this->denominator * f2.denominator;
//     display();
// }  
// };

// int main()
// {
//     // Fraction f1(4,0);
//     // cout<<f1.numerator<<endl;
//     // Fraction f2(3,6);
//     // f1 + f2;
//     // Fraction f3(5,8);
//     Fraction f3;
//     Fraction f4(f3);
//     f3.numerator = 8;
//     f4.numerator = 99;
//     cout<<endl<<f3.getNumerator()<<endl;
//     cout<<endl<<f4.getNumerator()<<endl;




// return 0;
// }

#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
 
using namespace std;
class Student
{
    public:
    int rn;
    int cls;
    Student(Student const &s) 
    {
        this->rn = s.rn;
        this->cls = s.cls;
    }
};

int main()
{
Student s1;
s1.rn = 6;
s1.cls = 9;
Student s2(s1);
s2.rn = 87;
cout<<s1.rn<<endl;
cout<<s2.rn<<endl;
    
return 0;
}