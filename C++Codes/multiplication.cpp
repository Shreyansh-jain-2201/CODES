#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
 
using namespace std;
 
int multiply(int a, int b)
{
    if(a == 0 || b == 0)
    {
        return 0;
    }
    // if(b == 1)
    // {
    //     return a;
    // }
    else
    {
        return a + multiply(a,b-1);
    }
}
int main()
{
    cout<<multiply(6,6)<<endl;
return 0;
}