// Write a program to read the Employee details of N persons with EMPID, EDEPT, and ESAL.  Print only those employee ID’s who are working in the “SALES” department drawing a salary of more than 25000.  [Use pointer to an array of structures].

#include <stdio.h>
#include <stdlib.h>

struct Employee
{
    int EMPID;
    char EDEPT[10];
    float ESAL;
};



int main()
{
    int i, n;
    struct Employee *ptr;
    printf("Enter the number of employees: ");
    scanf("%d", &n);
    ptr = (struct Employee *)malloc(n * sizeof(struct Employee));
    for (i = 0; i < n; i++)
    {
        printf("Enter the details of employee %d: \n", i + 1);
        printf("Enter the employee ID: ");
        scanf("%d", &ptr[i].EMPID);
        printf("Enter the employee department: ");
        scanf("%s", ptr[i].EDEPT);
        printf("Enter the employee salary: ");
        scanf("%f", &ptr[i].ESAL);
    }
    printf("The employee ID's who are working in the 'SALES' department and have a salary of more than 25000 are: \n");
    for (i = 0; i < n; i++)
    {
        if(ptr[i].EDEPT[0] == 'S' && ptr[i].EDEPT[1] == 'A' && ptr[i].EDEPT[2] == 'L' && ptr[i].EDEPT[3] == 'E' && ptr[i].EDEPT[4] == 'S' && ptr[i].ESAL > 25000)
        {
            printf("%d %s %f\n", ptr[i].EMPID,ptr[i].EDEPT, ptr[i].ESAL);
        }
    }
    return 0;
}