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
    int n, count = 0, capacity = 0, exit, enter;
    cin>>n;
    for (int i = 0; i < n; i++)
    {
        cin>>exit>>enter;
        count = count - exit + enter;
        if (count>capacity)
        {
            capacity = count;
        }
        enter = 0;
        exit = 0;
    }
    cout<<capacity<<endl;
return 0;
}