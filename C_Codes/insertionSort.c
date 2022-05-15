#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int patternMatch(char *str, char *substr, int len, int len1)
{
    int maxIndex = len - len1;
    int flag = 0;
    int i, j;
    for (i = 0; i <= maxIndex; i++)
    {
        for (j = 0; j < len1; j++)
        {
            if (str[i + j] != substr[j])
                break;
        }
        if (j == len1)
        {
            flag = 1;
            break;
        }
    }
    if (flag)
        return i;
    else
        return -1;
}

int main()
{
    char str[100], substr[50];
    printf("\n Enter Main String :");
    gets(str);
    printf("\n Enter Substring :");
    scanf(" %s", substr);
    int len = strlen(str);
    int len1 = strlen(substr);
    int index = patternMatch(str, substr, len, len1);
    if (index == -1)
    {
        printf("\n Pattern is not found!");
    }
    else
        printf("\n Pattern is found at %d position.", index);
}