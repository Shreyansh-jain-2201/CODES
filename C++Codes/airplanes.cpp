#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
 
using namespace std;
int main()
{
    int k,n,s,p,num;
    cin>>k>>n>>s>>p;
    if (n%s != 0)
    {
        n = s*(n/s + 1);
    }
    if ((n*k/s)%p != 0)
    {
        num = 1 + (n*k/s)/p;
    }
    else
    {
        num = (n*k/s)/p;
    }
    cout<<num;
return 0;
}
