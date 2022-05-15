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
void reverse(char s[], int n, int p, int i)
{
    if (i == n - 1)
    {
        for (int i = 0; i < p; i++)
        {
            cout << s[i] << "";
        }
        return;
    }
    else
    {
        char temp = s[i];
        s[i] = s[n - 1];
        s[n - 1] = temp;
        return reverse(s, n - 1, p, i + 1);
    }
}

int main()
{
    int n;
    cin >> n;
    char arr[n];

    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    reverse(arr, n, n, 0);
    return 0;
}