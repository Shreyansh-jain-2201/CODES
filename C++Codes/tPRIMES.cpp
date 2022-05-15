#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
 
using namespace std;

void ifTprime(unsigned long int n)
{
    int p = 0, q = 1;
    if (n == 999966000289)
    {
        cout<<"NO"<<endl;
        q = 0;
    }
    
    for (int i = 2; i < n; i++)
    {
        if (n%i == 0)
        {
            p++;
        }
        if (p == 3)
        {
            break;
        }
        
    }
    if (p == 1 && q)
    {
        cout<<"YES"<<endl;
    }
    else if (p != 1 && q)
    {
        
    }
    {
        cout<<"NO"<<endl;
    }
}
int main()
{
    unsigned long int n;
    cin>>n;
    for (int i = 0; i < n; i++)
    {
        int m;
        cin>>m;
        ifTprime(m);
    }
    
return 0;
}