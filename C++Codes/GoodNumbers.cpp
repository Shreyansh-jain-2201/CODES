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

// int checkSum(int numbers[12])
// {
// }
int main()
{
    int arr[61] = {1, 3, 5, 7, 9, 15, 17, 21, 27, 31, 33, 45, 51, 63, 65, 73, 85, 93, 99, 107, 119, 127, 129, 153, 165, 189, 195, 219, 231, 255, 257, 273, 297, 313, 325, 341, 365, 381, 387, 403, 427, 443, 455, 471, 495, 511, 513, 561, 585, 633, 645, 693, 717, 765, 771, 819, 843, 891, 903, 951, 975};
    int t;
    cin >> t;
    for (int p = 0; p < t; p++)
    {
        int num;
        cin >> num;
        int max = 0;
        int sum = 0;
        int q;
        for (int i = 0; i < 63; i++)
        {
            if (arr[i] > num)
            {
                break;
            }
            else
            {
                max = arr[i];
                q = i;
            }
        }
        cout << max << " ";
        sum = sum + max;
        if (num - sum <= 11)
        {
            while (sum < num)
            {
                cout << "1 ";
                sum++;
            }
        }
        else
        {
            while (num != sum)
            {

                for (int j = q; j >= 0; j--)
                {
                    if (arr[j] <= num - sum)
                    {
                        sum = sum + arr[j];
                        cout << arr[j] << ' ';
                    }
                    if (sum == num)
                    {
                        break;
                    }
                }
            }
        }
        cout << endl;
    }

    return 0;
}

// for (int k = 0; k < (num - sum) / arr[j]; k++)
// {
//     cout << arr[j] << " ";
//     sum = sum + arr[j];
//     if (sum >= num)
//         break;
// }
// for (int k = 0; k < num - sum; k++)
// {
//     cout << "1 ";
// }