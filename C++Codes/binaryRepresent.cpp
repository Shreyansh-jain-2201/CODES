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

int max(int num)
{
    int m = 0;
    int n = to_string(num).length();
    for (int i = 0; i < n; i++)
    {
        if (stoi(to_string(num).substr(i, 1)) > m)
        {
            m = stoi(to_string(num).substr(i, 1));
        }
    }
    return m;
}
int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;
        cout << max(num) << endl;
    }

    return 0;
}