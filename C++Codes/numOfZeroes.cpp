#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
 
using namespace std;
 
int num(int n)
{
    if (n < 10)
    {
        return 0;
    }
    else if ((n/10)*10 != n)
    {
        return num(n/10);
    }
    else
    {
        return 1 + num(n/10);
    }
}
int main()
{
    cout << num(10090);
    
return 0;
}