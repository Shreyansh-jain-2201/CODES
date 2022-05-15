#include <stdio.h>
#include <stdlib.h>

void alphabets(char Start, char End)
{
    if (Start <= End)
    {
        int i = Start;
        while (i <= End)
        {
            printf("%c ", i);
            i++;
        }
    }
    else
    {
        int i = Start;
        while (i <= 'z')
        {
            printf("%c ", i);
            i++;
        }
        i = 'a';
        while (i <= End)
        {
            printf("%c ", i);
            i++;
        }
    }
}

int main()
{
    char Start, End;
    scanf("%c %c", &Start, &End);
    alphabets(Start, End);
    return 0;
}