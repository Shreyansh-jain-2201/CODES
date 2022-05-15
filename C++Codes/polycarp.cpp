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
    int n;
    cin>>n;
    for (int i = 0; i < n; i++)
    {
        int a,b,c,n,p,num = 0,f = 0;
        string sum;
        cin>>a>>b>>c>>n;
        p = a + b + c + n;
        sum = to_string(p);
        for (int i = 0; i < sum.length(); i++)
        { 
            num = num + (int)sum[i];
        }
        int largest = a;
        if (largest<b) largest = b;
        if (largest<c) largest = c;
        if(((3*largest)-(a+b+c))<=n) f = 1;
        if(num%3 == 0 && f)
        {cout<<"YES"<<endl;}
        else
        {cout<<"NO"<<endl;}
    }
return 0;
}