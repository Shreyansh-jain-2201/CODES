// mim and max using divide and conquer
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

void MaxMin(int arr[], int low, int high, int &max1, int &min1)
{
    if (low == high)
    {
        max1 = arr[low];
        min1 = arr[high];
    }
    else if (low == high - 1)
    {
        if (arr[low] > arr[high])
        {
            max1 = arr[low];
            min1 = arr[high];
        }
        else
        {
            max1 = arr[high];
            min1 = arr[low];
        }
    }
    else
    {
        int mid = (low + high) / 2;
        int max2, min2;
        MaxMin(arr, low, mid, max1, min1);
        MaxMin(arr, mid + 1, high, max2, min2);
        if (max1 < max2)
        {
            max1 = max2;
        }
        if (min1 > min2)
        {
            min1 = min2;
        }
    }
}
int main()
{
    int n, max1 = INT_MAX, min1 = INT_MIN;
    cout << "Enter the number of element in your array: ";
    cin >> n;
    int arr[n + 1];
    cout << "Enter the elements of array: ";
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    MaxMin(arr, 0, n - 1, max1, min1);
    cout << "Maximum element in your array: " << max1 << endl;
    cout << "Minimum element in your array: " << min1 << endl;
    return 0;
}