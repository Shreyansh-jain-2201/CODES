#include <stdio.h>
#include <limits.h>

long int arr[20][20];
int s[20][20];
int p[20], i, j, n;

void matrix_chain_multiplication()
{
    long int q;
    int k;
    for (i = n; i > 0; i--)
    {
        for (j = i; j <= n; j++)
        {
            if (i == j)
                arr[i][j] = 0;
            else
            {
                for (k = i; k < j; k++)
                {
                    q = arr[i][k] + arr[k + 1][j] + p[i - 1] * p[k] * p[j];
                    if (q < arr[i][j])
                    {
                        arr[i][j] = q;
                    }
                }
            }
        }
    }
}

int main()
{
    int k;
    scanf("%d", &n);
    for (i = 1; i <= n; i++)
        for (j = i + 1; j <= n; j++)
        {
            arr[i][i] = 0;
            arr[i][j] = 99999999;
        }
    for (k = 0; k <= n; k++)
    {
        scanf("%d", &p[k]);
    }
    matrix_chain_multiplication();

    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= n; j++)
        {
            printf("%ld ", arr[i][j]);
        }
        printf("\n");
    }
    return 0;
}

// 5
// 4 10 3 12 20 7