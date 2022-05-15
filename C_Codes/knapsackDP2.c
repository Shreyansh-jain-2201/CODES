// 0/1 knapsack using dp

#include <stdio.h>

int max(int a, int b)
{
    if (a > b)
        return a;
    else
        return b;
}
int main()
{

    int value[500] = {0}, weight[500] = {0};
    int capacity, n;
    int k[500][500];

    printf("Enter the size of bag: ");
    scanf("%d", &capacity);
    printf("Enter the number of items: ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)
    {
        printf("Enter profit and weight of item %d: ", i);
        scanf("%d %d", &value[i], &weight[i]);
        // printf("Enter weight of item %d: ", i);
        // scanf("%d", &weight[i]);
    }

    for (int i = 0; i <= n; i++)
    {
        for (int w = 0; w <= capacity; w++)
        {
            if (i == 0 || w == 0)
                k[i][w] = 0;
            else if (weight[i] <= w)
                k[i][w] = max(value[i] + k[i - 1][w - weight[i]], k[i - 1][w]);
            else
                k[i][w] = k[i - 1][w];
        }
    }

    printf("The total value of the knapsack is: %d", k[n][capacity]);
    int i = n, j = capacity;

    while (i > 0)
    {
        if (k[i][j] == k[i - 1][j])
        {
            printf("\nItem %d = Not selected", i, "\n");
            i = i - 1;
        }
        else
        {
            printf("\nItem %d = Selected", i, "\n");
            j = j - weight[i];
            i = i - 1;
        }
    }
    return 0;
}
