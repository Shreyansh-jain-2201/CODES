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
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        int n;
        int ones = 0;
        int zeros = 0;
        cin >> n;
        int output = 0;
        for (int j = 0; j < n; j++)
        {
            // count consecutive zeros
            int x;
            cin >> x;
            if (x == 0)
            {
                zeros++;
            }
            else
            {
                ones++;
                output = output + zeros;
                zeros = 0;
            }
        }
        cout << output + 1 << endl;
    }
    return 0;
}