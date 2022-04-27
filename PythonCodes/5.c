// C program to delete a file

#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *fp;
    fp = fopen("C:\\Users\\Saurabh\\Desktop\\1.c", "r");
    if (fp == NULL)
    {
        printf("Error!");
        exit(1);
    }
    fclose(fp);
    remove("C:\\Users\\Saurabh\\Desktop\\1.c");
    return 0;
}