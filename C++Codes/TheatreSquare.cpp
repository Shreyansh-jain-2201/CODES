#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <climits>
#include <list>
#include <cmath>
#include <vector>
using namespace std;
unsigned long long int min(unsigned long long int a, unsigned long long int b, unsigned long long int c){
    unsigned long long int k;
    if(a%c == 0){
        if (b%c == 0)
        {
            k = (a/c) * (b/c);
        }
        else
        {
            k = (a/c) * (b/c + 1);
        }
        
    }
    else if (b%c == 0)
    {
        k = (a/c + 1) * (b/c);
    }
    else
    {
        k = (a/c + 1) * (b/c + 1);
    }
    return k;
    
}
int main()
{
    unsigned long long int a,b,c;
    cin>>a>>b>>c; 
    cout<<min(a,b,c);
return 0;
}