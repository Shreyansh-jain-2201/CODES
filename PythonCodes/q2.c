// Write a program to read the Employee details of N persons with EMPID, EDEPT, and ESAL.  Print only those employee ID’s who are working in the “SALES” department drawing a salary of more than 25000.  [Use pointer to an array of structures].

#include <stdio.h>
#include <stdlib.h>

struct Employee
{
    int empid;
    char dept[10];
    int sal;
};

int main()
{
    struct Employee *emp;
    int n, i, count = 0;
    printf("Enter the number of employees: ");
    scanf("%d", &n);
    emp = (struct Employee *)malloc(n * sizeof(struct Employee));
    for (i = 0; i < n; i++)
    {
        printf("Enter the details of employee %d: ", i + 1);
        scanf("%d %s %d", &emp[i].empid, emp[i].dept, &emp[i].sal);
    }
    for (i = 0; i < n; i++)
    {
        if (strcmp(emp[i].dept, "SALES") == 0 && emp[i].sal > 25000)
        {
            count++;
        }
    }
    printf("The number of employees working in the SALES department with salary more than 25000 is %d", count);
    return 0;
}