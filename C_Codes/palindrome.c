// write a c function to check whether the given string is a palindrome or not using static memory allocation using pointers

#include <stdio.h>
#include <string.h>

int isPalindrome(char *str)
{
    int i, j, k;
    char *str1, *str2;
    str1 = str;
    str2 = str;
    k = strlen(str);
    for (i = 0; i < k / 2; i++)
    {
        str1++;
    }
    for (j = k - 1; j >= k / 2; j--)
    {
        str2++;
    }
    if (strcmp(str1, str2) == 0)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
int main()
{
    char str[100];
    printf("Enter the string\n");
    scanf("%s", str);
    if (isPalindrome(str))
    {
        printf("String is a palindrome\n");
    }
    else
    {
        printf("String is not a palindrome\n");
    }
    return 0;
}