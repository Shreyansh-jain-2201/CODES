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

int gcd(int a, int b)
{
    if (b == 0)
    {
        return a;
    }
    else
    {
        return gcd(b, a % b);
    }
}

int noOfpairs(int k)
{
    int num = 0;
    for (int i = 0; i < k; i++)
    {
        int max = 0;
        for (int j = 0; j < min(k - i, i); j++)
        {
            if (abs(gcd(i, j) - gcd(k - i, j)) > max)
            {
                max = abs(gcd(i, j) - gcd(k - i, j));
            }
        }
        if (max == k)
        {
            num++;
        }
    }
    return num;
}
int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int k;
        cin >> k;
        cout << noOfpairs(k) << endl;
    }
    return 0;
}