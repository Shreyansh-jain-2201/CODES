#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
 
using namespace std;

bool ifNewYear(int year)
{
    int num,remain;
    if (year<2020)
    {
        return false;
    }
    else
    {
        num = year/2020;
        remain = year%2020;
        if (num>=remain)
        {
            return true;
        }
        else
        {
            return false;
        }
        
    }
}

int main()
{
    int n;
    cin>>n;
    int year[n];
    for (int i = 0; i < n; i++)
    {
        cin>>year[i];
        if (ifNewYear(year[i]))
        {
            cout<<"YES"<<endl;
        }
        else
        {
            cout<<"NO"<<endl;
        }
    }
    
return 0;
}