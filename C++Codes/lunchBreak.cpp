#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
 
using namespace std;

int joy(int f, int t, int k)
{
    if(t>k)
    { return f - (t-k); }
    else
    { return f;}
}
 
int main()
{
    int n,k,sum = -1000000000;
    cin>>n>>k;
    for(int i=0; i<n; i++){
        int f,t;
        cin>>f>>t;
        if(joy(f,t,k) > sum)
        {
            sum = joy(f,t,k);
        }
    }
    cout<<sum<<endl;
return 0;
}