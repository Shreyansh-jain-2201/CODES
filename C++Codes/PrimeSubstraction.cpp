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
    int t,f=0;
    cin>>t;
    for(int k=0;k<t;k++)
    {
        int x,y,n;
        cin>>x>>y;
        n=x-y;
        for(int i=2;i<=n;i++)
        {
            if(n%i==0)
            {
                for(int j=2;j<=i;j++)
                {
                    if(i%j==0)
                    f=f+1;
                }
                if(f==1)
                {
                 cout<<"YES"<<endl;
                 break;
                }

            }


        }
        if(f!=1)
            cout<<"NO"<<endl;
            f=0;

    }

return 0;
}