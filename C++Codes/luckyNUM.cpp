#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>

using namespace std;


void luckyNUM(int n){
    int arr[] = {4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777};
    int p = 0;

    for (int ik = 0; ik < 14; ik++)
    {
        if (arr[ik] > n)
        {
            break;
        }
        else if (n%arr[ik] == 0)
        {
            p++;
            break;
        }
        
    }
    if (p)
    {
        cout<<"YES"<<endl;
    }
    else
    {
        cout<<"NO"<<endl;
    }
}

int main()
{
    int n;
    cin>>n;
    luckyNUM(n);
return 0;
}