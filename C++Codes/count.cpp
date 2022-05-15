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
void print(int ans[])
{
    int i = 0;
    while (ans[i] != -1)
    {
        cout << ans[i] << " ";
        i = i + 1;
    }
    cout << endl;
}

void count(int arr[], int n, int x, int i, int ptr, int ans[])
{
    if (n == 0)
    {
        print(ans);
        return;
    }
    if (arr[0] == x)
    {
        ans[ptr] = i;
        return count(arr + 1, n - 1, x, i + 1, ptr + 1, ans);
    }
    else
    {
        return count(arr + 1, n - 1, x, i + 1, ptr, ans);
    }
}
bool checkPalindrome(int arr[], int n, int i)
{
    if (arr[n - 1] != arr[i])
    {
        return false;
    }
    else if (n < i)
    {
        return true;
    }
    else
    {
        return checkPalindrome(arr, n - 1, i + 1);
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
    // count(arr, n, x, 0, 0, ans);
    cout << checkPalindrome(arr, n, 0);
    return 0;
}