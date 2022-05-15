// #include<stdio.h>
// #include<stdlib.h>
// #include<pthread.h>
// #include<semaphore.h>
// #include<unistd.h>
// sem_t chopstick[5];
// void * philos(void *);
// void eat(int);
// int main()
//  {
//          int i,n[5];
//          pthread_t T[5];
//          for(i=0;i<5;i++)
//          sem_init(&chopstick[i],0,1);
//          for(i=0;i<5;i++){
//                  n[i]=i;
//                  pthread_create(&T[i],NULL,philos,(void *)&n[i]);
//                  }
//          for(i=0;i<5;i++)
//                  pthread_join(T[i],NULL);
//  }
// void * philos(void * n)
//  {
//          int ph=*(int *)n;
//          printf("Philosopher %d wants to eat\n",ph);
//          printf("Philosopher %d tries to pick left chopstick\n",ph);
//          sem_wait(&chopstick[ph]);
//          printf("Philosopher %d picks the left chopstick\n",ph);
//          printf("Philosopher %d tries to pick the right chopstick\n",ph);
//          sem_wait(&chopstick[(ph+1)%5]);
//          printf("Philosopher %d picks the right chopstick\n",ph);
//          eat(ph);
//          sleep(2);
//          printf("Philosopher %d has finished eating\n",ph);
//          sem_post(&chopstick[(ph+1)%5]);
//          printf("Philosopher %d leaves the right chopstick\n",ph);
//          sem_post(&chopstick[ph]);
//          printf("Philosopher %d leaves the left chopstick\n",ph);
//  }
//  void eat(int ph)
//  {
//          printf("Philosopher %d begins to eat\n",ph);
//  }

// #include <stdio.h>
// #include<limits.h>
// #define INFY 999999999
// long int m[20][20];
// int s[20][20];
// int p[20],i,j,n;

// void print_optimal(int i,int j)
// {
// if (i == j)
// printf(" A%d ",i);
// else
//    {
//       printf("( ");
//       print_optimal(i, s[i][j]);
//       print_optimal(s[i][j] + 1, j);
//       printf(" )");
//    }
// }

// void matmultiply(void)
// {
// long int q;
// int k;
// for(i=n;i>0;i--)
//  {
//    for(j=i;j<=n;j++)
//     {
//      if(i==j)
//        m[i][j]=0;
//      else
//        {
//         for(k=i;k<j;k++)
//         {
//          q=m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j];
//          if(q<m[i][j])
//           {
//             m[i][j]=q;
//             s[i][j]=k;
//           }
//          }
//         }
//       }
//  }
// }

// int MatrixChainOrder(int p[], int i, int j)
// {
//     if(i == j)
//         return 0;
//     int k;
//     int min = INT_MAX;
//     int count;

//     for (k = i; k <j; k++)
//     {
//         count = MatrixChainOrder(p, i, k) +
//                 MatrixChainOrder(p, k+1, j) +
//                 p[i-1]*p[k]*p[j];

//         if (count < min)
//             min = count;
//     }

//     // Return minimum count
//     return min;
// }

// void main()
// {
// int k;
// printf("Enter the no. of elements: ");
// scanf("%d",&n);
// for(i=1;i<=n;i++)
// for(j=i+1;j<=n;j++)
// {
//  m[i][i]=0;
//  m[i][j]=INFY;
//  s[i][j]=0;
// }
// printf("\nEnter the dimensions: \n");
// for(k=0;k<=n;k++)
// {
//  printf("P%d: ",k);
//  scanf("%d",&p[k]);
// }
// matmultiply();
// printf("\nCost Matrix M:\n");
// for(i=1;i<=n;i++)
//  for(j=i;j<=n;j++)
//   printf("m[%d][%d]: %ld\n",i,j,m[i][j]);

// i=1,j=n;
// printf("\nMultiplication Sequence : ");
// print_optimal(i,j);
// printf("\nMinimum number of multiplications is : %d ",
//                           MatrixChainOrder(p, 1, n));

// }

// 2
// 3
// 4
// 5
// 6
// 7
// 8
// 9
// 10
// 11
// 12
// 13
// 14
// 15
// 16
// 17
// 18
// 19
// 20
// 21
// 22
// 23
// 24
// 25
// 26
// 27
// 28
// 29
// 30
// 31
// 32
// 33
// 34
// 35
// 36
// 37
// 38
// 39
// 40
// 41
// 42
// 43
// 44
// 45
// 46
// 47
// 48
// 49
// 50
// 51
// 52
// 53
// 54
// 55
// 56
// 57
// 58
// 59
// 60
// 61
// 62
// This code implemented using Algorithm in Coremen book

#include <stdio.h>
#include <limits.h>

// Matrix Ai has dimension p[i-1] x p[i] for i = 1..n

int MatrixChainMultiplication(int p[], int n)
{
        int m[n][n];
        int i, j, k, L, q;

        for (i = 1; i < n; i++)
                m[i][i] = 0; //number of multiplications are 0(zero) when there is only one matrix

        //Here L is chain length. It varies from length 2 to length n.
        for (L = 2; L < n; L++)
        {
                for (i = 1; i < n - L + 1; i++)
                {
                        j = i + L - 1;
                        m[i][j] = INT_MAX; //assigning to maximum value

                        for (k = i; k <= j - 1; k++)
                        {
                                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j];
                                if (q < m[i][j])
                                {
                                        m[i][j] = q; //if number of multiplications found less that number will be updated.
                                }
                        }
                }
        }

        return m[1][n - 1]; //returning the final answer which is M[1][n]
}

int main()
{
        int n, i;
        printf("Enter number of matrices\n");
        scanf("%d", &n);

        n++;

        int arr[n];

        printf("Enter dimensions \n");

        for (i = 0; i < n; i++)
        {
                printf("Enter d%d :: ", i);
                scanf("%d", &arr[i]);
        }

        int size = sizeof(arr) / sizeof(arr[0]);

        printf("Minimum number of multiplications is %d ", MatrixChainMultiplication(arr, size));

        return 0;
}