// #include <math.h>
// #include <stdio.h>

// void display(int arr[], int n)
// {
//     int i;
//     for (i = 0; i < n; i++)
//         printf("%d ", arr[i]);
//     printf("\n");
// }
// void insertionSort(int arr[], int n)
// {
//     int i, key, j;
//     display(arr, n);
//     for (i = 1; i < n; i++)
//     {
//         key = arr[i];
//         j = i - 1;
//         while (j >= 0 && arr[j] > key)
//         {
//             arr[j + 1] = arr[j];
//             j = j - 1;
//         }
//         arr[j + 1] = key;
//         display(arr, n);
//     }
// }

// int main()
// {
//     int n;
//     scanf("%d", &n);
//     int arr[n];
//     for (int i = 0; i < n; i++)
//     {
//         scanf("%d", &arr[i]);
//     }

//     insertionSort(arr, n);
//     return 0;
// }

// #include <stdio.h>
// int main()
// {
//     char str[80], subs[20];
//     int c1 = 0, c2 = 0, i, j, flg;
//     fgets(str, sizeof str, stdin);
//     fgets(subs, sizeof subs, stdin);

//     while (str[c1] != '\0')
//         c1++;
//     c1--;

//     while (subs[c2] != '\0')
//         c2++;
//     c2--;

//     for (i = 0; i <= c1 - c2; i++)
//     {
//         for (j = i; j < i + c2; j++)
//         {
//             flg = 1;
//             if (str[j] != subs[j - i])
//             {
//                 flg = 0;
//                 break;
//             }
//         }

//         if (flg == 1)

//             break;
//     }
//     if (flg == 1)
//         printf("%d", i);
//     else
//         printf("-1");
//     return 0;
// }

// #include <stdio.h>
// #include <limits.h>

// #define infinity 999999999
// long int matrix[100][100];
// int p[100], i, j, n;

// void MultiplyMatrices(void)
// {
//     long int q;
//     int k;
//     for (i = n; i > 0; i--)
//     {
//         for (j = i; j <= n; j++)
//         {
//             if (i == j)
//                 matrix[i][j] = 0;
//             else
//             {
//                 for (k = i; k < j; k++)
//                 {
//                     q = matrix[i][k] + matrix[k + 1][j] + p[i - 1] * p[k] * p[j];
//                     if (q < matrix[i][j])
//                     {
//                         matrix[i][j] = q;
//                     }
//                 }
//             }
//         }
//     }
// }

// int main()
// {
//     int k;
//     scanf("%d", &n);
//     for (i = 1; i <= n; i++)
//         for (j = i + 1; j <= n; j++)
//         {
//             matrix[i][i] = 0;
//             matrix[i][j] = infinity;
//         }
//     for (k = 0; k <= n; k++)
//     {
//         scanf("%d", &p[k]);
//     }
//     MultiplyMatrices();

//     for (i = 1; i <= n; i++)
//     {
//         for (j = 1; j <= n; j++)
//         {
//             printf("%ld ", matrix[i][j]);
//         }
//         printf("\n");
//     }
//     return 0;
// }