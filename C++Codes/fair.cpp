#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
 
using namespace std;
int gcd(int a,int b)
{
    if (a == 0)
        return b;
    return gcd(b % a, a);
}

int lcm(int num[])
{
    fo
}
 
int makefair(int n)
{
    string s = to_string(n);
    for(int i = 0; i <= s.length(); i++)
    {
        if(s.substr(i) == "0")
        {
            continue;
        }
        else
    }
}
int main()
{
    
return 0;
}