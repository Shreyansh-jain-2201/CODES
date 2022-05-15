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
    int mishka = 0, chris = 0, n,m,c;
    cin>>n;
    for (int i = 0; i < n; i++)
    {
        m = 0;
        c = 0;
        cin>>m>>c;
        if (m>c)
        {
            mishka++;
        }
        else if (c>m)
        {
            chris++;
        }
        
    }
    if (mishka > chris)
    {
        cout<<"Mishka"<<endl;
    }
    else if (chris > mishka)
    {
        cout<<"Chris"<<endl;
    }
    else
    {
        cout<<"Friendship is magic!^^"<<endl;
    }
    
    
return 0;
}