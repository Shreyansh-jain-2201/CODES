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
    int a, b;
double n;
    cin>>a>>b;
    n = ceil((log(b) - log(a))/log(1.5));
    if (pow(3,n)*a > pow(2,n)*b)
    {
        cout<<n<<endl;
    }
    else{
        cout<<n+1<<endl;
    }
    

return 0;
}