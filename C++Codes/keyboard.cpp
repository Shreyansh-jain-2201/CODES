#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
 
using namespace std;

string left(string s1, string position)
{
    string s2 = "qwertyuiopasdfghjkl;zxcvbnm,./";
    string output;
    for (int i = 0; i < s1.length(); i++)
    {
        if (position == "L")
        {
            output = output + s2.substr(s2.find(s1.substr(i,1)) + 1,1);
        }
        else
        {
            output = output + s2.substr(s2.find(s1.substr(i,1)) - 1,1);
        }
    }
    return output;
}

int main()
{
    string s2,s1;
    cin>>s2>>s1;
    cout<<left(s1,s2)<<endl;
    
return 0;
}