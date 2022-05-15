#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
 
using namespace std;

int calculate(unsigned long long int a, unsigned long long int b)
{
    int p = 0;
    if(b == 1)
    {
        b = 2;
        p = 1;
    }
    int count = log(a)/log(b) + 1;
    int x = 0;
    int output = count + 1;
    for(int i = 0; i<=count; i++)
    {
        x = b + i;
        for(int j = 0; j<=count; j++)
        {
            if (pow(x, j) > a && i+j < output)
            {
                output = i + j;
                
            }
        }
    }
    if(pow(x, output + p) == a)
    {
        output = output + p + 1;
    }
    else
    {
        output = output + p;
    }
    return output;
}
 
 
int main()
{
    int n;
    cin>>n;
    for(int i = 0; i<n;i++)
    {
        unsigned long long int a,b;
        cin>>a>>b;
        cout<<calculate(a, b)<<endl;
    }
return 0;
}