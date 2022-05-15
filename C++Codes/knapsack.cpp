#include <iostream>
#include <algorithm>

using namespace std;

int knapsack(int weight[], int value[], int capacity, int n)
{
    if (n == 0 || capacity == 0)
    {
        return 0;
    }
    if (weight[n - 1] > capacity)
    {
        return knapsack(weight, value, capacity, n - 1);
    }
    else
    {
        return max(knapsack(weight, value, capacity, n - 1), value[n - 1] + knapsack(weight, value, capacity - weight[n - 1], n - 1));
    }
}

int main()
{
    int weight[] = {10, 20, 30};
    int value[] = {60, 100, 120};
    int capacity = 50;
    int n = 3;
    cout << knapsack(weight, value, capacity, n);
    return 0;
}
