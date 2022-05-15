#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
#include<algorithm>
 
using namespace std;
int main()
{
    string word1,word2;
    int count =0;
    cin>>word1;
    cin>>word2;
    transform(word1.begin(), word1.end(), word1.begin(), ::tolower);
    transform(word2.begin(), word2.end(), word2.begin(), ::tolower);
    for (int i = 0; i < word1.length(); i++)
    {
        if (word1[i]>word2[i])
        {
            cout<<'1'<<endl;
            count++;
            break;
        }
        else if(word1[i]<word2[i])
        {
            cout<<-1<<endl;
            count++;
            break;
        }
    }
    if (count == 0)
    {
        cout<<'0'<<endl;
    }
    
    
return 0;
}