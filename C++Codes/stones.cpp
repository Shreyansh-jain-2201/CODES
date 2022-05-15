#include <iostream>
#include <string.h>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include<algorithm>
#include <vector>
 
using namespace std;
int main()
{
    string s;
    int num, count = 0;
    cin>>num;
    cin>>s;
    
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == s[i+1])
        {
            count = count + 1;
        }
        
    }
    cout<<count;
return 0;
}