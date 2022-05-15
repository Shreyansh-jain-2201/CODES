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

int sum(int arr[], int n)
{

    if (n == 1)
    {
        return arr[0];
    }
    else
    {
        return arr[0] + sum(arr + 1, n - 1);
    }
}

int isPresent(int arr[], int n, int x, int i)
{

    if (n == 0)
    {
        return -1;
    }
    if (arr[i] == x)
    {
        return i;
    }
    else
    {
        return isPresent(arr, n - 1, x, i - 1);
    }
}
int main()
{
    int n;
    cin >> n;
    int x;
    cin >> x;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    cout << isPresent(arr, n, x, n - 1);
    return 0;
}