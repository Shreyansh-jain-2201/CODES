#include <stdio.h>
#include <stdlib.h>

void powerConsumptionCost(int units, int *cost)
{
    if (units <= 100)
        *cost = units * 1 + 50;
    else if (units > 100 && units <= 200)
        *cost = (units - 100) * 3 + 2 * 100 + 100;
    else if (units > 200 && units <= 500)
        *cost = 100 * 7 + (units - 200) * 5 + 200;
    else
        *cost = 100 * 7 + (units - 200) * 5 + 200;
}

int main()
{
    int units, cost;
    scanf("%d", &units);
    powerConsumptionCost(units, &cost);
    printf("%d", cost);
    return 0;
}