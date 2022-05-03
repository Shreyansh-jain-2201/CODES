// Create a structure data type for the customers of electricity with the fields: Connection Number (integer), Customer Name, customer type (one character   C- commercial, D- Domestic, I- Industry, E-Education), and Units Consumed.  Make use of the pointers to structure concepts to read the N customer details and Print only the commercial customer name who have consumed more than 700 units.
// For example:

// Test	Input	Result
// 1
// 4
// 101 RAJA C 1000 
// 102 RANI D 1000
// 103 SACHIN I 1000
// 104 RAHUL E 1000
// RAJA

#include <stdio.h>
#include <stdlib.h>

struct Customer
{
    int conno;
    char name[20];
    char type;
    int units;
};

int main()
{
    struct Customer *cust;
    int n, i, count = 0;
    scanf("%d", &n);
    cust = (struct Customer *)malloc(n * sizeof(struct Customer));
    for (i = 0; i < n; i++)
    {
        scanf("%d %s %c %d", &cust[i].conno, cust[i].name, &cust[i].type, &cust[i].units);
    }
    // Name of customers who have consumed more than 700 units
    for (i = 0; i < n; i++)
    {
        if (cust[i].type == 'C' && cust[i].units > 700)
        {
            printf("%s\n", cust[i].name);
        }
    }
    return 0;
}