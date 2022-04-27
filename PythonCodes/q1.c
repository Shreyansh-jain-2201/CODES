// Write a program to read a string and perform the following using pointers

// a.       Count the number of letters and words – print the same,

// b.      Count the number of vowels and print the same,

// c.       Count the number of characters (other than vowels) – print the same

// Count the number of white spaces – print the same
// For example:

// Test	Input	Result
// 1
// Vellore Institute
// 17 2 7 10 1

#include <stdio.h>
#include <stdlib.h>

int countVowels(char *str)
{
    int count = 0;
    while (*str != '\0')
    {
        if (*str == 'a' || *str == 'e' || *str == 'i' || *str == 'o' || *str == 'u' || *str == 'A' || *str == 'E' || *str == 'I' || *str == 'O' || *str == 'U')
        {
            count++;
        }
        str++;
    }

    return count;
}

int countConsonants(char *str)
{
    int count = 0;
    while (*str != '\0')
    {
        if (*str != 'a' && *str != 'e' && *str != 'i' && *str != 'o' && *str != 'u' && *str != 'A' && *str != 'E' && *str != 'I' && *str != 'O' && *str != 'U')
        {
            count++;
        }
        str++;}
    return count;
}

int countLetters(char *str)
{
    int count = 0;
    while (*str != '\0')
    {
        count++;
        str++;
    }
    return count;
}

int countWords(char *str)
{
    int count = 0;
    while (*str != '\0')
    {
        if (*str == ' ')
        {
            count++;
        }
        str++;
    }
    return count + 1;
}

int countWhiteSpaces(char *str)
{
    int count = 0;
    while (*str != '\0')
    {
        if (*str == ' ')
        {
            count++;
        }
        str++;
    }
    return count;
}

int main()
{
    char str[100];
    scanf("%[^\n]s", str);  
    char *p = str;
    printf("%d %d %d %d %d\n", countLetters(p), countWords(p), countVowels(p), countConsonants(p), countWhiteSpaces(p));
    return 0;
}