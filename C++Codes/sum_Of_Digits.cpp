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

int sum(int n)
{
    cout << n << endl;
    int num = 0;
    if (to_string(n).length() == 1)
    {
        return n;
    }
    else
    {
        for (int i = 0; i < to_string(n).length(); i++)
        {
            num = num + stoi(to_string(n).substr(i, 1));
        }
        return sum(num);
    }
}

int main()
{
    cout << sum(99999999999);
    return 0;
}