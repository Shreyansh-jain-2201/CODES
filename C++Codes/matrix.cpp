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
    int binary,num,a,b;
    for (int i = 1; i < 6; i++)
    {
        for (int j = 1; j < 6; j++)
        {
            cin>>binary;
            if (binary == 1)
            {
                a = i;
                b = j;

            }
            binary = 0;
            
        }
        
    }
    num = abs(3 - a) + abs(3 - b);
    cout<<num<<endl;
    
return 0;
}