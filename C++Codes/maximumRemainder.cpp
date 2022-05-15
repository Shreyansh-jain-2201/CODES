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
// function to return gcd of two numbers
int gcd(int a, int b)
{
    if (a == 0)
        return b;
    return gcd(b % a, a);
}

int main()
{
    int t;
    cin >> t;
    for (int w = 0; w < t; w++)
    {

        int n;
        cin >> n;
        int max = 0;
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                if (i != j && gcd(i, j) > max)
                {
                    max = gcd(i, j);
                    cout << i << " " << j << " " << max << endl;
                }
            }
        }
    }

    return 0;
}