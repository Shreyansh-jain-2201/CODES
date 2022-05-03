// C Program to print contents of file

#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *fp;
    int c;
    fp = fopen("C:\\Users\\Saurabh\\Desktop\\1.c", "r");
    if (fp == NULL)
    {
        printf("Error!");
        exit(1);
    }
    while ((c = getc(fp)) != EOF)
    {
        printf("%c", c);
    }
    fclose(fp);
    return 0;
}