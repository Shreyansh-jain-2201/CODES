#include <stdio.h>
#include <stdlib.h>

struct student
{
    char subject[80];
    int marks;
};

int main()
{
    int n;
    printf("Enter the number of subjects: ");
    scanf("%d", &n);
    struct student *ptr = (struct student *)malloc(n * sizeof(struct student));
    for (int i = 0; i < n; i++)
    {
        printf("Enter the name and marks of subject: ");
        scanf("%s", &(ptr + i)->subject);
        scanf("%d", &(ptr + i)->marks);
    }
    for (int i = 0; i < n; i++)
    {
        printf("%s\t", (ptr + i)->subject);
        printf("%d\n", (ptr + i)->marks);
    }
    free(ptr);
    ptr = NULL;
}

// #include <stdio.h>
// #include <string.h>
// #include <stdlib.h>

// struct student
// {
//     char subject[99];
//     int marks;
// };

// int main()
// {
//     struct student course;
//     int n;
//     scanf("%d", &n);
//     struct student *ptr = (struct student *)malloc(n * sizeof(struct student));
//     for (int i = 0; i < n; i++)
//     {
//         scanf("%s", &(ptr + i)->subject);
//         scanf("%d", &(ptr + i)->marks);
//     }
//     for (int i = 0; i < n; i++)
//     {
//         printf("Subject= %s\n", (ptr + i)->subject);
//         printf("Mark= %d\n", (ptr + i)->marks);
//     }
//     free(ptr);
//     ptr = NULL;
//     return 0;
// }