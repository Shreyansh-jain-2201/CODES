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
    for (int k = 0; k < t; k++)
    {
        double n;
        cin >> n;
        int p = int(n);
        int output = 0;
        for (int i = 0; i < p; i++)
        {
            double val = n / 2;
            int ans = int(n / 2);
            if (val == ans)
            {
                output = output + 1;
                n = n / 2;
            }
            else
            {
                break;
            }
        }
        cout << output << endl;
    }
    return 0;
}