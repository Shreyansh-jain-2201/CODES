#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

void reverse(string &s, int start, int end)
{
    while (start < end)
    {
        swap(s[start], s[end]);
        start++;
        end--;
    }
}
bool isPossible(int k, string s1, string s2, int s)
{
    if (s == k)
    {
        return true;
    }
    else if (s1.size() == 0)
    {
        return false;
    }
    else if (s1[0] == s2[0])
    {
        s1 = s1.substr(1);
        s2 = s2.substr(1);
        return (isPossible(k + 1, s1, s2, s));
    }
    else
    {
        s1 = s1.substr(1);
        return (isPossible(k, s1, s2, s));
    }
}

// bool isPossible(string s1, string s2)
// {
//     int n = s1.size();
//     int m = s2.size();
//     reverse(s1, 0, n - 1);
//     reverse(s2, 0, m - 1);
//     int k = 0;
//     int p = 0;
//     int i = 0;
//     int j = 0;
//     while (i <= m && j <= n)
//     {
//         if (s2[i] == s1[j])
//         {
//             k++;
//             i++;
//             j++;
//         }
//         j++;
//     }
//     if (k == m)
//     {
//         return true;
//     }
//     return false;
// }

int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        string s1, s2;
        cin >> s1 >> s2;
        int k = 0, n = s2.size(), m = s1.size();
        reverse(s1, 0, m - 1);
        reverse(s2, 0, n - 1);
        if (isPossible(k, s1, s2, n))
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }
}