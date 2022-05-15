// write a c function to check whether the given string is a palindrome or not using dynamic memory allocation using pointers

#include <string.h>
#include <stdio.h>
#include <stdlib.h>

// Function to check whether the given string is a palindrome or not
// Using dynamic memory allocation

void isPalindrome(char *str)
{
    int i, j, k;
    char *str1, *str2;
    str1 = (char *)malloc(sizeof(char) * 100);
    str2 = (char *)malloc(sizeof(char) * 100);
    strcpy(str1, str);
    strcpy(str2, str);
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
        printf("String is a palindrome\n");
    }
    else
    {
        printf("String is not a palindrome\n");
    }
}

int main()
{
    char str[100];
    scanf("%s", &str);
    isPalindrome(str);
    return 0;
}