#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>

 
using namespace std;
 
class Complex
{
private:
    /* data */
public:
    int a,b;
    Complex(int a, int b)
    {
        this->a = a;
        this->b = b;
    }
    void display()
    {
        cout<<this->a<<"+i"<<this->b;
    }
    
    void operator+ (Complex C)
    {
        this->a = this->a + C.a;
        this->b = this->b + C.b;
    }

};

int main()
{
    int a,b,c,d;
    string str1, str2;
    cin>>str1>>str2;
    char f = 'i';
    int ind1 = str1.find(f);
    int ind2 = str2.find(f);
    a = stoi(str1.substr(0, ind1));
    b = stoi(str1.substr(ind1+1));
    c = stoi(str2.substr(0, ind2));
    d = stoi(str2.substr(ind2+1));

    Complex C1(a,b);
    Complex C2(c,d);
    C1+C2;
    C1.display();

return 0;
}