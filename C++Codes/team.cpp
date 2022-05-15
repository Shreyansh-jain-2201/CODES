#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
 
using namespace std;

int ifSure(int a, int b, int c){
    if ((a + b + c) >= 2)
    {
        return 1;
    }
    else
    {
        return 0;
    }
    
}
int main()
{
    int n;
    cin>>n;
    int count = 0;
    for (int i = 0; i < n; i++)
    {
        int a,b,c;
        cin>>a>>b>>c;
        count += ifSure(a,b,c);
    }
    cout<<count<<endl;
    
return 0;
}