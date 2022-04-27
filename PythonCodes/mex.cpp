#include <iostream>
using namespace std;

int count(int arr[], int n, int x)
{
    int c = 0;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == x)
            c++;
    }
    return c;
}

// int smallest(int arr[], int n, int x)
// {
//     int small;
//     for (int i = 0; i < n; i++)
//     {
//         if (arr[i] > x)
//         {
//             small = arr[i];
//             break;
//         }
//     }
//     for (int i = 0; i < n; i++)
//     {
//         if (arr[i] < small && arr[i] > x)
//             small = arr[i];
//     }
//     return small;
// }

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int n;
        cin >> n;
        int arr[2 * n];
        for (int j = 0; j < 2 * n; j++)
        {
            cin >> arr[j];
        }
        bool isPossible = true;
        int x = 0;
        for (int j = 0; j < n; j++)
        {
            int c = count(arr, 2 * n, x);
            if (c % 2 != 0)
            {
                isPossible = false;
                break;
            }
            if (c == 0)
            {
                isPossible = true;
                break;
            }
            x++;
        }
        if (isPossible)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
}