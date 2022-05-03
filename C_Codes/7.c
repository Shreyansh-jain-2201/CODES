// Print a pattern of numbers from 1 to n as shown below.
// // Each of the numbers is separated by a single space.

// Input Format
// The input will contain a single integer n
// Sample Input 
// 2

// Sample Output

// 2 2 2
// 2 1 2
// 2 2 2

#include <stdio.h>
#include <stdlib.h>

void pattern (int n)
{
    int i, j, k;
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= n; j++)
        {
            for (k = 1; k <= n; k++)
            {
                if (i == j && j == k)
                {
                    printf("%d ", i);
                }
            }
        }
        printf("\n");
    }
}


int main()
{
    int n;
    scanf("%d", &n);
    pattern(n);
    return 0;
}