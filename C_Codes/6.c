//  C Program to list all files and sub-directories in a directory

#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>

int main()
{
    DIR *dir;
    struct dirent *ent;
    if ((dir = opendir(".")) != NULL)
    {
        while ((ent = readdir(dir)) != NULL)
        {
            printf("%s\n", ent->d_name);
        }
        closedir(dir);
    }
    else
    {
        perror("");
        exit(EXIT_FAILURE);
    }
    return 0;
}