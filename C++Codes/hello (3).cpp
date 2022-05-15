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
    string hello,word,match = "hello";
    cin>>word;
    int j = 0;
    for (int i = 0; i < word.length(); i++)
    {
        if (word[i] == match[j])
        {
            hello = hello + match[j];
            j ++;
            if (j == 5)
            {
                cout<<"YES"<<endl;
                break;
            }
            
        }
    }
    if (j<5)
    {
        cout<<"NO"<<endl;
    }
    
return 0;
}