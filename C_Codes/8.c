// Write a program to append the contents of one file at the end of
// another.

#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *fp1, *fp2;
    int c;
    fp1 = fopen("C:\\Users\\Saurabh\\Desktop\\1.c", "r");
    if (fp1 == NULL)
    {
        printf("Error!");
        exit(1);
    }
    fp2 = fopen("C:\\Users\\Saurabh\\Desktop\\3.c", "a");
    if (fp2 == NULL)
    {
        printf("Error!");
        exit(1);
    }
    while ((c = getc(fp1)) != EOF)
    {
        putc(c, fp2);
    }
    fclose(fp1);
    fclose(fp2);
    return 0;
}