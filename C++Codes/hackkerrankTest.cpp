#include <iostream>
#include <vector>
#include <set>
using namespace std;

int check(vector<int> arr)
{
    set<int> s;
    vector<int> vec;
    unsigned size = arr.size();
    for (unsigned i = 0; i < size; ++i)
    {
        s.insert(arr[i]);
    }
    vec.assign(s.begin(), s.end());
    int n = vec.size();
    if (n > 2)
    {
        return 0;
    }
    if (n == 2)
    {
        if (abs(vec.at(0) - vec.at(1)) < 2)
        {
            return arr.size();
        }
        else
        {
            return 0;
        }
    }
    return arr.size();
}
int main()
{

    int n;
    cin >> n;
    int max = 0;
    vector<int> arr;
    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;
        arr.insert(arr.begin() + i, num);
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = i; j < n; j++)
        {
            vector<int> v;
            v.assign(arr.begin() + i, arr.begin() + j);
            if (check(v) > max)
            {
                max = check(v);
            }
        }
    }
    cout << max << endl;
    return 0;
}