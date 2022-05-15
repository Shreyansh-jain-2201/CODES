#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;

void display(vector<int> arr)
{
    int n = arr.size();
    for (int i = 0; i < n; i++)
    {
        cout << arr.at(i) << " ";
    }
    cout << endl;
}

int main()
{
    vector<int> v;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        v.push_back(i + 1);
    }
    display(v);
    return 0;
}