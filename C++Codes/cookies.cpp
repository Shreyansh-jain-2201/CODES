#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
 
using namespace std;
bool isEven(int arr[], int n, int i)
{
    int sum = 0;
    for (int j = 0; j < n; j++)
    {
        if(i != j)
        {
            sum = sum + arr[j];
        }
    }
    if (sum%2 == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}
 
int main()
{
    int n;
    int output = 0;
    cin >> n;
    int arr[n];
    for (int i = 0; i<n; i++)
    {
        cin>>arr[i];
    }
    for (int i = 0; i<n; i++)
    {
        if(isEven(arr, n, i))
        {
            output = output + 1;
        }
    }
    cout<<output;
return 0;
}