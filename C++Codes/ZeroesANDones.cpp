#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
 
using namespace std;

int output(string num)
{
    string s1 = "01";
    string s2 = "10";
    while (strstr(num.c_str(),s1.c_str()) || strstr(num.c_str(),s2.c_str()))
    {
        if (strstr(num.c_str(),s1.c_str()))
        {
            int i = num.find(s1);
            num = num.substr(0,i) + num.substr(i + 2,num.length() - (i+2));
        }
        else if (strstr(num.c_str(),s2.c_str()))
        {
            int i = num.find(s2);
            num = num.substr(0,i) + num.substr(i + 2,num.length() - (i+2));
        }
    }
    return num.length();
}

int main()
{
    int n;
    cin>>n;
    char m[n];
    cin>>m;
    cout<<output(m);
return 0;
}