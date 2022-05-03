// Write a C program that will return the number of times a word is present in the original string.  
// For example:  
// Original String:  Vellore institute is a top ranked institute in India. 
// Word to be searched: institute 
// Output: 2 (institute occurs 2 times in the original string)

#include <stdio.h>
#include <string.h>

int countWord(char *str, char *word)
{
    int count = 0;
    int i = 0;
    int j = 0;
    int len = strlen(word);
    while (str[i] != '\0')
    {
        while (str[i] == word[j])
        {
            i++;
            j++;
        }
        if (j == len)
        {
            count++;
            j = 0;
        }
        else
        {
            i = i - j + 1;
            j = 0;
        }
    }
    return count;
}

int main()
{
    char str[100], word[100];
    printf("Enter the string: ");
    scanf("%[^\n]", str);
    getchar();
    printf("Enter the word to be searched: ");
    scanf("%[^\n]", word);
    getchar();
    printf("%d", countWord(str, word));
    return 0;
}