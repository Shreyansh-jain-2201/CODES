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
    int n,m,no_of_moves;
    cin>>n>>m;
    if(n%2 == 0)
    {
        no_of_moves = n/2;
    }
    else
    {
        no_of_moves = n/2 + 1;
    }
    if(no_of_moves%m == 0)
    {
        cout<<no_of_moves;
    }
    else
    {
        if(n<m)
        {
            cout<<"-1";
        }
        else if((no_of_moves + m -(no_of_moves + m)%m)%m == 0 && (no_of_moves + m -(no_of_moves + m)%m) <= n)
        {
            cout<<no_of_moves + m -(no_of_moves + m)%m;
        }
        else
        {
            cout<<"-1";
        }
    }

return 0;
}