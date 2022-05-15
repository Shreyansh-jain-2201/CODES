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
    int n;
    cin>>n;
    for (int i = 0; i < n; i++) 
    {
        int candies, kids, num, remain;
        cin >> candies>>kids;
        num = (candies/kids)*kids;
        remain = candies - num;
        cout<<num + min(kids/2, remain)<<endl;
    }
return 0;
}