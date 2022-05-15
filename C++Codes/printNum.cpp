#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
 
using namespace std;
 
void printNum(int n)
{
    if(n == 0)
    {
        return;
    }
    printNum(n-1);
    cout<<n<<" ";
}
int main()
{
printNum(5);
return 0;
}

