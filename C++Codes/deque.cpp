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

void display(deque<int> array)
{
    int n = array.size();
    for (int i = 0; i < n; i++)
    {
        cout<<array.at(i)<<" ";
    }
    cout<<endl;
}

void max(int n, int a, deque<int> array)
{
    deque<int> output;
    for (int i = 0; i < n-a+1; i++)
    {
        deque<int> subarray;
        for (int j = 0; j < a; j++)
        {
            subarray.push_back(array.at(i+j));
        }
        sort(subarray.begin(), subarray.end());
        output.push_back(subarray.at(subarray.size()-1));
    }
    display(output);
}

int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        deque<int> array;
        int t,a;
        cin >>t>>a;
        for(int j = 0; j<t; j++)
        {
            int element;
            cin >> element;
            array.push_back(element);
        }
        max(t,a,array);
    }

return 0;
}