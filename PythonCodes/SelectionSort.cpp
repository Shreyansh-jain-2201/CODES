#include<iostream>

using namespace std;

// void swap(int *arr, int p, int q)
// {
//     int temp = arr[p];
//     arr[p] = arr[q];
//     arr[q] = temp;
// }

int smallest(int *arr, int n)
{
    int small = arr[0];
    int j = 0;
    for(int i = 0; i<n; i++)
    {
        if(arr[i]< small)
        {
            small = arr[i];
            j = i;
        }
    }
    return j;
}
void SelectionSort(int* arr, int n)
{
    int k = 0;
    for (int i = 0; i < n-1; i++)
    {
        int q = smallest(arr+k, n-k);
        if(arr[k]<arr[q])
        {
            swap(arr[k], arr[q]);
        }
        k++;
    }
}
int main()
{
    int arr[] = {2,3,5,2,1,3,4,1,12};
    SelectionSort(arr, 9);
    // swap(arr[1],arr[5]);
    for (int i = 0; i < 9; i++)
    {
        cout<<arr[i]<<" ";
    }
    
}