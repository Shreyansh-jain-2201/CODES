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
    int a,b,c,n,count_a=0, count_b=0, count_c=0;
    cin>>n;
    for (int i = 0; i < n; i++)
    {
        cin>>a>>b>>c;
        count_a = count_a + a;
        count_b = count_b + b;
        count_c = count_c + c;
    }
    if (count_a == 0 && count_b == 0 && count_c == 0)
    {
        cout<<"YES"<<endl;
    }
    else
    {
        cout<<"NO"<<endl;
    }
    

return 0;
}