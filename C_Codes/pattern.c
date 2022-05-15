#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    char arr[1000];
    char *p = arr;
    scanf("%s", p);
    p = &arr[strlen(arr) - 1];
    while (*p)
    {
        printf("%c", *p);
        p--;
    }
}