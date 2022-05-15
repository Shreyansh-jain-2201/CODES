#include <iostream>

using namespace std;

int main()
{
    int n, p;
    cin >> n >> p;
    int output = 0;
    int arr[n][p];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i][0];
        cin >> arr[i][1];
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (double(arr[i][0]) / double(arr[j][0]) == double(arr[i][1]) / double(arr[j][1]))
            {
                output = output + 1;
            }
        }
    }
    cout << output;

    return 0;
}
// #include <iostream>
// #include <string>
// #include <algorithm>

// using namespace std;

// bool isSorted(string s)
// {
//     int n = s.length();
//     char c[n];

//     for (int i = 0; i < n; i++)
//     {
//         c[i] = s[i];
//     }
//     sort(c, c + n);

//     for (int i = 0; i < n; i++)
//         if (c[i] != s[i])
//             return false;
//     return true;
// }

// int main()
// {
//     int n;
//     cin >> n;
//     for (int i = 0; i < n; i++)
//     {
//         string s;
//         cin >> s;
//         if (isSorted(s))
//         {
//             cout << "NO" << endl;
//         }
//         else
//         {
//             cout << "YES" << endl;
//         }
//     }
//     return 0;
// }