#include <iostream>
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

    return 0;
}
using namespace std;

int cv(char a[], int n)
{
    int output = 0;
    for (int i = 0; i < n; i++)
    {
        if (a[i] != 'a' && a[i] != 'e' && a[i] != 'i' && a[i] != 'o' && a[i] != 'u')
        {
            if (a[i + 1] == 'a' || a[i + 1] == 'e' || a[i + 1] == 'i' || a[i + 1] == 'o' || a[i + 1] == 'u')
            {
                output = output + 1;
            }
        }
    }
    return output;
}

int main()
{
    string p = "hello";
    cout << p[p.length() - 2];
    // int t;
    // cin >> t;
    // for (int i = 0; i < t; i++)
    // {
    //     int n;
    //     cin >> n;
    //     char a[n];
    //     cin >> a;
    //     cout << cv(a, n) << endl;
    // }
    return 0;
}