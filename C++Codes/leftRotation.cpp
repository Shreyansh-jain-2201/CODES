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
void print(vector<int> arr)
{
    int n = arr.size();
    for (int i = 0; i < n; i++)
    {
        cout << arr.at(i) << " ";
    }
}
void lr(vector<int> arr, int n, int d)
{
    vector<int> newArr;
    for (int i = 0; i < n; i++)
    {
        newArr.push_back(arr.at((i + d) % n));
    }
    print(newArr);
}
int main()
{
    int n, d;
    cin >> n >> d;
    vector<int> arr;
    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;
        arr.push_back(num);
    }
    lr(arr, n, d);

    return 0;
}