#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
 
using namespace std;

int sixtwo(long long int num)
{
    int three = 0, two = 0;
    while (num > 1)
    {
        if (num == 1)
        {
            break;
        }
        
        else if (num%3 == 0)
        {
            num = num/3;
            three++;
        }
        else if (num%2 == 0)
        {
            num = num/2;
            two++;
        }
    }
    if (2*three - two > 0 && num == 1)
    {
        return 2*three - two;
    }
    else
    {
        return - 1;
    }
}
int main()
{
    long int n;
    cin>>n;
    for (int i = 0; i < n; i++)
    {
        long long int m;
        cin>>m;
        cout<<sixtwo(m)<<endl;
    }
return 0;
}