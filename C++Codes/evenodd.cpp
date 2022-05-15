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
    unsigned long long int n, k;
    cin>>n>>k;
    if ((n+1)/2 >= k)
    {
        cout<<(2*k) - 1<<endl;
    }
    else
    {
        k = k - ((n+1)/2);
        cout<<2*k<<endl;
    }
    
    
return 0;
}