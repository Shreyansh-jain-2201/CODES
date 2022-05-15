#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <map>
#include <deque>
#include <cstdio>

using namespace std;

// function to find the factorial of a number
int factorial(int n)
{
    if (n == 0)
        return 1;
    else
        return (n * factorial(n - 1));
}
// function to find the nth term of the series
int nthTerm(int n)
{
    int sum = 0;
    for (int i = 1; i <= n; i++)
    {
        sum = sum + (factorial(i) / (factorial(i - 1) * factorial(i - 1)));
    }
    return sum;
}
// function to sort the array using quick sort
// function to sort the array using quick sort
void quickSort(int arr[], int low, int high)
{
    // quick sort is based on the pivot element
    // pivot element is the element at the middle of the array
    int pivot = arr[(low + high) / 2];
    int i = low;
    int j = high;
    while (i <= j)
    {
        // if the element at the left of the pivot is less than the pivot
        // then increment the left index
        while (arr[i] < pivot)
            i++;
        // if the element at the right of the pivot is greater than the pivot
        // then decrement the right index
        while (arr[j] > pivot)
            j--;
        // if the left index is less than or equal to the right index
        // then swap the elements at the left and right index
        if (i <= j)
        {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
            j--;
        }
    }
}
int main()
{
    int t;
    cin >> t;
    for (int k = 0; k < t; k++)
    {
        double n;
        cin >> n;
        int p = int(n);
        int output = 0;
        for (int i = 0; i < p; i++)
        {
            double val = n / 2;
            int ans = int(n / 2);
            if (val == ans)
            {
                output = output + 1;
                n = n / 2;
            }
            else
            {
                break;
            }
        }
        cout << output << endl;
    }
    return 0;
}