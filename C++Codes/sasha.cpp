#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <map>
#include <deque>
#include <cstdio>

using namespace std;


int main()
{
    int n,v,cost;
    cin>>n>>v;
    if (n <= v) 
    {
        cout<<n-1<<endl;
    }
    else
    {
        n = n - v - 1;
        cost = v + (n*(n+1)/2) + n;
        cout<<cost<<endl;
    }
return 0;
}
