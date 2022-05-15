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

int staircase(int n)
{
    if (n == 0 || n == 1)
    {
        return 1;
    }
    if (n == 2)
    {
        return 2;
    }
    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3);
}
int towerOfHanoi(int n)
{
    if (n == 1)
    {
        return 1;
    }
    return 2 * towerOfHanoi(n - 1) + 1;
}

int main()
{
    int n;
    cin >> n;
    cout << staircase(n) << endl;
    cout << towerOfHanoi(n);
    return 0;
}