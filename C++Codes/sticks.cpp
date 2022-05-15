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
    int m,n,o;
    cin>>m>>n;
    if (m>n)
    {
        o = n;
    }
    else
    {
        o = m;
    }
    
    if (o%2 == 0)
    {
        cout<<"Malvika"<<endl;
    }
    else
    {
        cout<<"Akshat"<<endl;
    }
    
return 0;
}
