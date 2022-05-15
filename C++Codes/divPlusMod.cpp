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

// fa(x)=⌊x/a⌋+xmoda, where ⌊x/a⌋ is x/a, rounded down, x moda — the remainder of the integer division of x by a.
int func(int x, int a)
{
    return (x / a) + (x % a);
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        int max = 0;
        int l, r, a;
        cin >> l >> r >> a;
        max = func(r, a);
        cout << max << endl;
    }
    return 0;
}