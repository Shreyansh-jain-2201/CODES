#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
 
using namespace std;
bool payment(unsigned long long int a, unsigned long long int b, unsigned long long int n, unsigned long long int s)
{
    unsigned long long int c = s/n;
    if (c>a)
    {
        c = a;
    }
    if(a*n + b < s)
    { return false;}
    if(s - c*n <= b)
    { return true;}
    else
    return false;
}
 
int main()
{
    int q;
    cin>>q;
    for(int i=0; i<q; i++)
    {
        unsigned long long int a,b,n,s;
        cin>>a>>b>>n>>s;
        if(payment(a,b,n,s))
        cout<<"YES"<<endl;
        else
        cout<<"NO"<<endl;
    }

return 0;
}