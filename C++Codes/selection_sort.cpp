#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
 
using namespace std;

 
int main()
{
    int n;
    cin>>n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin>>arr[i];
    }
    for (int i = 0; i < n-1; i++)
    {
        int temp;
        int smallest = arr[i+1];
        int p = i+1;
        for (int j = i+1; j < n; j++)
        {
            if (arr[j] < smallest)
            {
                smallest = arr[j];
                p = j;
            }
        }
        if (arr[i]>smallest)
        {
            temp = arr[i];
            arr[i] = arr[p];
            arr[p] = temp;
        }
    }
    for (int i = 0; i < n; i++)
    {
        cout<<arr[i]<<" ";
    }
return 0;
}