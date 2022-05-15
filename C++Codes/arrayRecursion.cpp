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

int reduce(int arr[], int n)
{
    int newArr[n - 1];
    for (int i = 1; i < n; i++)
    {
        newArr[i - 1] = arr[i];
    }
    return newArr[n - 1];
}

bool check(int arr[], int n)
{
    if (n == 0 || n == 1)
    {
        return true;
    }
    else if (arr[0] > arr[1])
    {
        return false;
    }
    else
    {
        // int arrNew = reduce(arr, n);
        return check(arr + 1, n - 1);
    }
}
int main()
{
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    cout << check(arr, n);

    return 0;
}