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

void waves(int arr[], int n)
{
    int p = 0;
    int q = n - 1;
    int temp[n];
    for (int i = 0; i < n; i++)
    {
        temp[i] = arr[i];
    }
    for (int i = 0; i < n; i++)
    {
        if (temp[i])
        {
            arr[q] = 1;
            q--;
        }
        else
        {
            arr[p] = 0;
            p++;
        }
        if (p > q)
        {
            break;
        }
    }
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
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
    waves(arr, n);
    return 0;
}