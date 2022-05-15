#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
 
using namespace std;

// int max(int arr[], int n){

//     int maxElement = arr[0];
//     for (int i = 0; i <n; i++)
//     {
//         if (arr[i] > maxElement)
//         {
//             maxElement = arr[i];
//         }
        
//     }
//     return maxElement;
// }
int main()
{
    int n;
    int arr[1000];
    cin>>n;
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        cin>>arr[i];
    }
    int max = arr[0];
    for (int i = 0; i <n; i++)
    {
        if (arr[i] > max)
        {
            max = arr[i];
        }
        
    }
    for (int i = 0; i < n; i++)
    {
        sum = sum + (max - arr[i]);
    }
    cout<<sum<<endl;
    
return 0;
}