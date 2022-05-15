#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
 
using namespace std;
int sum(int n)
{
    if (n < 10)
    {
        return n;
    }
    else
    {
        return n%10 + sum(n/10);
    }
}
 
int main()
{
    cout << sum(1235)<<endl;
return 0;
}