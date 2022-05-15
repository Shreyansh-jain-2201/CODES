#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
 
using namespace std;
int count(int n, string list[], string s)
{
    int count = 0;
    for(int i = 0; i < n; i++)
    {
        if(list[i] == s)
        { count++;}
    }
    return count;
}
 
int main()
{
    int n;
    cin>>n;
    string list[n];
    for(int i = 0; i < n; i++)
    {
        cin>>list[i];
    }
    int goals = 0;
    string winner;
    for(int i = 0; i < n; i++)
    {
        if(goals<count(n,list,list[i]))
        {
        goals = count(n,list,list[i]);
        winner = list[i];
        }
    }
    cout<<winner;
return 0;
}