#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>

using namespace std;

int OddSum(int num)
{
    string output, s;
    int sum = 0;
    while (num != 0)
    {
        s = to_string(num % 2);
        num = num / 2;
        output = output + s;
    }
    for (int i = 0; i < output.length() / 2; i++)
    {
        swap(output[i], output[output.length() - i - 1]);
    }
    for (int i=0; i<output.length(); i++)
    {
        if (i%2==0 && output[i]=='1')
        {
            sum ++;
        }
        
    }

    return sum;
}

int main()
{
    int t,n,k,p,j;
    cin>>t;
    for (int i = 0; i < t; i++)
    {
        p = 1;
        j = 0;
        k = 0;
        cin>>n;
        while (p)
        {
            j++;
            k = k + OddSum(j);
            if (k>=n)
            {
                cout<<j<<endl;
                p = 0;
            }
            
        }
        
    }

    return 0;
}