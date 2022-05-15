#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
 
using namespace std;

void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

void bubbleSort(int arr[], int n)
{
    int i, j;
    for (i = 0; i < n-1; i++)
    { 
        for (j = 0; j < n-i-1; j++)
        {
            if (arr[j] > arr[j+1])
            {
                swap(&arr[j], &arr[j+1]);
            }
        }
    }
}

int main()
{
    int sum = 0;
    int n,m;
    cin>>n>>m;
    int prices[n];
    for (int i = 0; i < n; i++)
    {
        cin>>prices[i];
    }
    bubbleSort(prices,n);
    for (int i = 0; i < m; i++)
    {
        if (prices[i] >= 0)
        {
            break;
        }
        else
        {
            sum = sum + prices[i];
        }
    }
    sum = -sum;
    cout<<sum;
return 0;
}