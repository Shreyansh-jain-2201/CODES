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
    int n,b,d,sum = 0,p = 0;
    cin>>n>>b>>d;
    int oranges[n];
    for (int i = 0; i < n; i++)
    {
        cin>>oranges[i];
        if (oranges[i] <= b)
        {
            sum = sum + oranges[i];
        }
        if (sum>d)
        {
            sum = 0;
            p++;
        }
        
    }
    cout<<p;
    
return 0;
}