// C++ implementation of fractional knapsack problem using greedy approach
#include <iostream>
using namespace std;

void knapsack(int n, float wt_obj[], float profit_obj[], float capacity)
{
    float vector[20], total_profit = 0;
    int i, j, cap;
    cap = capacity;
    for (i = 0; i < n; i++)
    {
        vector[i] = 0.0;
    }
    for (i = 0; i < n; i++)
    {
        if (wt_obj[i] > cap)
            break;
        else
        {
            vector[i] = 1.0;
            total_profit = total_profit + profit_obj[i];
            cap = cap - wt_obj[i];
        }
    }
    if (i < n)
    {
        vector[i] = cap / wt_obj[i];
    }
    total_profit = total_profit + (vector[i] * profit_obj[i]);
    cout << "\nThe result vector is: ";
    for (i = 0; i < n; i++)
    {
        cout << " " << vector[i];
    }
    cout << "\nThe maximum proft is: " << total_profit;
}
int main()
{
    float wt_obj[20], profit_obj[20], capacity;
    float num;
    int i, j;
    float ratio[20], temp;
    cout << "Enter the number of objects: ";
    cin >> num;
    cout << "Enter the weights and profit of each object: ";
    for (i = 0; i < num; i++)
        cin >> wt_obj[i] >> profit_obj[i];
    cout << "Enter the capacity of the knapsack: ";
    cin >> capacity;
    for (i = 0; i < num; i++)
    {
        ratio[i] = profit_obj[i] / wt_obj[i];
        cout << " " << ratio[i];
    }
    for (i = 0; i < num; i++)
    {
        for (j = i + 1; j < num; j++)
        {
            if (ratio[i] < ratio[j])
            {
                temp = ratio[j];
                ratio[j] = ratio[i];
                ratio[i] = temp;

                temp = wt_obj[j];
                wt_obj[j] = wt_obj[i];
                wt_obj[i] = temp;

                temp = profit_obj[j];
                profit_obj[j] = profit_obj[i];
                profit_obj[i] = temp;
            }
        }
    }

    knapsack(num, wt_obj, profit_obj, capacity);

    return 0;
}