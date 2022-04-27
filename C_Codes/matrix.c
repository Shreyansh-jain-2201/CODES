// Write a c program to add and multiply two n*m matrices using pointers.

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, m;
    printf("Enter the number of rows and columns of the matrix: ");
    scanf("%d %d", &n, &m);
    int **matrix1 = (int **)malloc(n * sizeof(int *));
    int **matrix2 = (int **)malloc(n * sizeof(int *));
    int **matrix3 = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; i++)
    {
        matrix1[i] = (int *)malloc(m * sizeof(int));
        matrix2[i] = (int *)malloc(m * sizeof(int));
        matrix3[i] = (int *)malloc(m * sizeof(int));
    }
    printf("Enter the elements of the first matrix: \n");
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf("%d", &matrix1[i][j]);
        }
    }
    printf("Enter the elements of the second matrix: \n");
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf("%d", &matrix2[i][j]);
        }
    }
    printf("The first matrix is: \n");
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            printf("%d ", matrix1[i][j]);
        }
        printf("\n");
    }
    printf("The second matrix is: \n");
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            printf("%d ", matrix2[i][j]);
        }
        printf("\n");
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            matrix3[i][j] = matrix1[i][j] + matrix2[i][j];
        }
    }
    printf("The sum of the two matrices is: \n");
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            printf("%d ", matrix3[i][j]);
        }
        printf("\n");
    }
    // multiplication
    int **matrix4 = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; i++)
    {
        matrix4[i] = (int *)malloc(m * sizeof(int));
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            matrix4[i][j] = 0;
            for (int k = 0; k < m; k++)
            {
                matrix4[i][j] += matrix1[i][k] * matrix2[k][j];
            }
        }
    }
    printf("The product of the two matrices is: \n");
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            printf("%d ", matrix3[i][j]);
        }
        printf("\n");
    }
    return 0;
    
}