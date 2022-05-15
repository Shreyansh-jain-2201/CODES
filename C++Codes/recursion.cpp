#include <iostream>
 
using namespace std;
 
int count(int n)
{
    if(n < 10)
    {
        return 1;
    }
    else
    {
        return count(n/10) + 1;
    }
}
int main()
{
    cout<<count(1056470);
return 0;
}