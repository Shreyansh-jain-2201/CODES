// Write a c program to find first n fibonacci numbers using dynamic programming.
#include <stdio.h>
#include <stdlib.h>

void fibonacci(int n)
{
    int f[n+1];
    f[0] = 0;
    f[1] = 1;
    for(int i = 2; i <= n; i++)
    {
        f[i] = f[i-1] + f[i-2];
    }
    for(int i = 0; i <= n; i++)
    {
        printf("%d ", f[i]);
    }
}

int main()
{
    int n;
    printf("Enter the number of terms: ");
    scanf("%d", &n);
    fibonacci(n);
    return 0;
}