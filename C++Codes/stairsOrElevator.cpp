#include <iostream>

using namespace std;

int main()
{
    int x,y,z,t1,t2,t3;

    cin>>x>>y>>z>>t1>>t2>>t3;
    int stairs = abs(x - y)*t1; 
    int elevator = (abs(x - z) + abs(x-y))*t2 + 3*t3;

    if (elevator<=stairs)
    {
        cout<<"YES";
    }

    else 
    {
        cout<<"NO";
    }

    return 0;
}