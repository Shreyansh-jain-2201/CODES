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
    string s;
    int count = 0, output = 0;
    cin>>s;
    for (int i = 0; i < s.length(); i++)
    {
        for (int j = i; j < s.length(); j++)
        {
            if (s[i] == s[j])
            {
                count++;
            }
            
        }
        if (count == 1)
        {
            output++;
        }
        count = 0;
        
    }
    if (output%2 == 0)
    {
        cout<<"CHAT WITH HER!"<<endl;
    }
    else{
        cout<<"IGNORE HIM!"<<endl;
    }
    
return 0;
}