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
    int n,sum = 0;
    cin>>n;
    for (int i = 1; i <= n/2; i++)
    {
        if ((n-i)%i == 0)
        {
            sum++;
        }
        
    }
    cout<<sum;
return 0;
}