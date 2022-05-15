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
    unsigned long int sum = 0, p = 1;
    unsigned long int n, t;
    int arr[n];
    cin>>n>>t;
    for (int i = 0; i < n-1; i++)
    {
        int num;
        cin>>num;
        sum = sum + num;
        if (sum == t)
        {
            cout<<"YES"<<endl;
            p = 0;
            break;
        }
        else if (sum > t && p)
        {
            cout<<"NO"<<endl;
            p = 0;
            break;
        }
        
    }
    if (p)
    {
        cout<<"NO"<<endl;
    }
    
return 0;
}