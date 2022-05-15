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
void print(vector<string> v)
{
    for (int i = 0; i < v.size(); i++)
    {
        cout << v.at(i) << " ";
    }
}
void print1(double c[], int p)
{
    for (int i = 0; i < p; i++)
    {
        cout << c[i] << " ";
    }
}

void trades(int n, vector<string> v, vector<string> s)
{
    double count[n];
    vector<string> output;
    int p = 0;
    for (int i = 0; i < s.size(); i++)
    {
        count[i] = 0;
        int k = 0;
        for (int j = 0; j < s.size(); j++)
        {
            while (s.at(j) == v.at(k))
            {
                count[i] = count[i] + 1;
                k++;
            }

            v.assign(v.begin() + k, v.end());
            int k = 0;
        }
        // count[i] = count[i] * 100 / n;
        if (count[i] >= 5)
        {
            output.insert(output.begin() + p, s.at(i));
            p++;
        }
        p++;
    }
    print(output);
    print1(count, p);
}

int main()
{
    int n;
    cin >> n;
    vector<string> v, s;
    set<string> s1;
    for (int i = 0; i < n; i++)
    {
        string p;
        cin >> p;
        v.insert(v.begin() + i, p);
        s1.insert(p);
    }
    s.assign(s1.begin(), s1.end());
    sort(s.begin(), s.end());
    sort(v.begin(), v.end());
    // print(v);
    // print(s);
    trades(n, v, s);
    return 0;
}