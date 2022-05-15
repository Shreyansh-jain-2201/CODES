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
    int count = 0;
    cin>>s;
    if (s.length()<7)
    {
        cout<<"NO"<<endl;
    }
    else
    {
        for (int i = 0; i < s.length() - 6; i++)
        {
            if (s.substr(i, 7) == "1111111" || s.substr(i, 7) == "0000000")
            {
                cout<<"YES"<<endl;
                count++;
                break;
            }
            
        }

        if (count == 0)
        {
            cout<<"NO"<<endl;
        }
        
    }
    
return 0;
}