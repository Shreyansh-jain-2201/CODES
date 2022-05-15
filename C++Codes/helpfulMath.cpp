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
    string num,num1,num2,num3,output;
    cin>>num;
    for (int i = 0; i < num.length(); i++)
    {
        if (num[i] == '1')
        {
            num1 = num1 + '1';
        }
        else if (num[i] == '2')
        {
            num2 = num2 + '2';
        }
        else if (num[i] == '3')
        {
            num3 = num3 + '3';
        }
    }
    num = num1+num2+num3;
    for (int i = 0; i < num.length(); i++)
    {
        if (i < num.length() - 1)
        {
            output = output + num[i] + '+';
        }
        else{
            output = output + num[i];
        }
    }
    cout<<output<<endl;
return 0;
}