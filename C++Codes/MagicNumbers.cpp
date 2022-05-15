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
    string n;
    cin >> n;
    int p = 1;
    while(n.length() > 0 && p)
    {
        if(n.substr(0, 3) == "144")
        {
            n = n.substr(3, n.length());
        }
        else if(n.substr(0, 2) == "14")
        {
            n = n.substr(2, n.length());
        }
        else if(n.substr(0, 1) == "1")
        {
            n = n.substr(1, n.length());
        }
        else
        {
            p = 0;
        }
    }
    if(p)
    {
        cout << "YES";
    }
    else
    {
        cout<< "NO";
    }
return 0;
}