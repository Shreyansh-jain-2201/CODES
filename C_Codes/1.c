// C Program to count number of lines in a file

#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *fp;
    int c, nl;
    fp = fopen("C:\\Users\\Saurabh\\Desktop\\1.c", "r");
    if (fp == NULL)
    {
        printf("Error!");
        exit(1);
    }
    nl = 0;
    while ((c = getc(fp)) != EOF)
    {
        if (c == '\n')
            nl++;
    }
    printf("Number of lines: %d", nl);
    fclose(fp);
    return 0;
}