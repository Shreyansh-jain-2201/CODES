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
    int n,p=0;
    cin>>n;
    string matrix[n];
    for (int i = 0; i < n; i++)
    {
        cin>>matrix[i];
    }
    for (int i = 0; i < n; i++)
    {
        if (matrix[i].substr(0,2) == "OO")
        {
            matrix[i] = "++" + matrix[i].substr(2);
            p++;
            break;
        }
        else if (matrix[i].substr(3) == "OO")
        {
            matrix[i] = matrix[i].substr(0,3) + "++";
            p++;
            break;
        }
    }
    if (p)
    {
        cout<<"YES"<<endl;
        for (int i = 0; i < n; i++)
        {
            cout<<matrix[i]<<endl;
        }
    }
    else
    {
        cout<<"NO"<<endl;
    }
    
return 0;
}