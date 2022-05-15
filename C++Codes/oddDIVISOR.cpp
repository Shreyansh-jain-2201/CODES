#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
 
using namespace std;
void ifodd(long long int n)
{
    long long int p, i;
    for (i = 1; i < n; i = i+2)
    {
        if (n%i == 0)
        {
            int m = n/i;
            if (i * m == n)
            {
                cout<<"YES"<<endl;
                cout<<i;
                break;
            }
            
        }
        
    }
    
}
int main()
{
    ifodd(1099511627776);
return 0;
}