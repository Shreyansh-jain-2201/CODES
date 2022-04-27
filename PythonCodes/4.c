//  C Program to merge contents of two files into a third file

#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *fp1, *fp2, *fp3;
    int c;
    fp1 = fopen("C:\\Users\\Saurabh\\Desktop\\1.c", "r");
    if (fp1 == NULL)
    {
        printf("Error!");
        exit(1);
    }
    fp2 = fopen("C:\\Users\\Saurabh\\Desktop\\2.c", "r");
    if (fp2 == NULL)
    {
        printf("Error!");
        exit(1);
    }
    fp3 = fopen("C:\\Users\\Saurabh\\Desktop\\3.c", "w");
    if (fp3 == NULL)
    {
        printf("Error!");
        exit(1);
    }
    while ((c = getc(fp1)) != EOF)
    {
        putc(c, fp3);
    }
    while ((c = getc(fp2)) != EOF)
    {
        putc(c, fp3);
    }
    fclose(fp1);
    fclose(fp2);
    fclose(fp3);
    return 0;
}