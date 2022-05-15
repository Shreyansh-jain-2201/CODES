#include <iostream>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
using namespace std;

void abbr(string word){
    cout<<word[0]<<word.length() - 2<<word[word.length()-1]<<endl;
}


int main()
{
    char word;
    int n,i;
    cin >> n;
    string list[n];
    for (i = 0; i < n; i++)
    {
        cin>> list[i];
    }
    for (i = 0; i < n; i++)
    {
        if (list[i].length()>10)
        {
            abbr(list[i]);
        }
        else
        {
            cout<<list[i]<<endl;
        }
        
    }
    
    return 0;
}