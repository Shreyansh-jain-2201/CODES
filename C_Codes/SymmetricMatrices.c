// // Write a C program to check if a given matrix is symmetric or not.

// #include<stdio.h>
// #include<stdlib.h>

// int main()
// {
//     int i, j, n, flag = 0;
//     printf("Enter the order of the matrix: ");
//     scanf("%d", &n);
//     int a[n][n];
//     printf("Enter the elements of the matrix: \n");
//     for (i = 0; i < n; i++)
//     {
//         for (j = 0; j < n; j++)
//         {
//             scanf("%d", &a[i][j]);
//         }
//     }
//     for (i = 0; i < n; i++)
//     {
//         for (j = 0; j < n; j++)
//         {
//             if (a[i][j] != a[j][i])
//             {
//                 flag = 1;
//                 break;
//             }
//         }
//     }
//     if (flag == 0)
//     {
//         printf("The matrix is symmetric.\n");
//     }
//     else
//     {
//         printf("The matrix is not symmetric.\n");
//     }
//     return 0;
// }
#include<stdio.h>  
// void change(int num) {    
//     printf("Before adding value inside function num=%d \n",num);    
//     num=num+100;    
//     printf("After adding value inside function num=%d \n", num);    
// }    
// int main() {    
//     int x=100;    
//     printf("Before function call x=%d \n", x);    
//     change(x);//passing value in function    
//     printf("After function call x=%d \n", x);    
// return 0;  
// }
// void CollatzConjecture(unsigned long long int n, unsigned long long int count) 
// {
//     printf("The value of n is %llu and the count is %llu\n", n, count);
//     if (n == 1)
//     {
//         printf("The Collatz Conjecture is true\n");
//     }
//     else if (n % 2 == 0)
//     {
//         CollatzConjecture(n / 2, count + 1);
//     }
//     else
//     {
//         CollatzConjecture(3 * n + 1, count + 1);
//     }
// }

// int main()
// {
//     unsigned long long int n;
//     unsigned long long int count = 1;
//     printf("Enter the value of n: ");
//     scanf("%llu", &n);
//     CollatzConjecture(n, count);
//     return 0;
// }

// create a function that takes variable number of arguments and returns the sum of all the arguments
// #include<stdio.h>
// #include<stdlib.h>
// #include <stdarg.h>

// int sum(int n, ...)
// {
//     int i, sum = 0;
//     va_list vl;
//     va_start(vl, n);
//     for (i = 0; i < n; i++)
//     {
//         sum = sum + (int)__builtin_va_arg(vl,int);
//     }
//     va_end(vl);
//     return sum;

// }

// int main()
// {
//     int n, sum1 = 0;
//     printf("Enter the number of arguments: ");
//     scanf("%d", &n);
//     sum1 = sum(n, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
//     printf("The sum is %d\n", sum);
//     return 0;
// }
#include <stdio.h>
#include <stdarg.h>

#define MAX(x,y) ((x)<(y)? (x):(y))

double average(int num,...) {

   va_list valist;
   double sum = 0.0;
   int i;

   /* initialize valist for num number of arguments */
   va_start(valist, num);

   /* access all the arguments assigned to valist */
   for (i = 0; i < num; i++) {
      sum += va_arg(valist, int);
   }
	
   /* clean memory reserved for valist */
   va_end(valist);

   return sum;
}

int main() {
   printf("Average of 2, 3, 4, 5 = %f\n", average(4, 2,3,4,5));
   printf("Average of 5, 10, 15 = %f\n", average(3, 5,10,15));
   printf("%d",MAX(5+99,10+100));
   return 0;
}
