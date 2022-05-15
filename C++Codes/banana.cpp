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
    int k,n,w,cost;
    cin>>k>>n>>w;
    if ((w*(w + 1)*k/2)-n >= 0)
    {
        cout<<(w*(w + 1)*k/2)-n<<endl;
    }
    else{
        cout<<'0'<<endl;
    }
return 0;
}