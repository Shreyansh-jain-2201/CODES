// 0/1 knapsack using dp

#include <iostream>
#include <string>
#include <cstring>
#include <cmath>

using namespace std;

int maximum(int a, int b)
{

    if (a > b)
    {
        return a;
    }
    return b;
}

int knapsack(int W, int weight[], int value[], int n)
{
    int i;
    int m;
    int K[n + 1][W + 1];

    for (i = 0; i <= n; i++)
    {
        for (m = 0; m <= W; m++)
        {
            if (i == 0 || m == 0)
                K[i][m] = 0;

            else if (weight[i - 1] <= m)
                K[i][m] = maximum(value[i - 1] + K[i - 1][m - weight[i - 1]], K[i - 1][m]);

            else
                K[i][m] = K[i - 1][m];
        }
    }

    return K[n][W];
}
int main()
{
    int n, W;
    cout << "Enter the number of items and the total capacity: ";
    cin >> n >> W;
    int weight[n], values[n];
    for (int i = 0; i < n; i++)
    {
        cout << "Enter the weight and value of item " << i + 1 << ": ";
        cin >> weight[i] >> values[i];
    }
    cout << "The total value of the knapsack is: " knapsack(W, weight, values, n);
    return 0;
}