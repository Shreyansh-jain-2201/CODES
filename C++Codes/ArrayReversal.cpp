#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
 
using namespace std;
void reverseArray(int n, int m, int arr[])
{
    int output[n];
    if (m>n)
    {
        m = m%n;
    }
    
    
    for (int i = 0; i < m; i++)
    {
        int temp = arr[0];
       for (int j = 0; j < n-1; j++)
       {
           arr[j] = arr[j + 1];
       }
       arr[n-1] = temp;
    }
    for (int i = 0; i < n; i++)
    {
        cout<<arr[i]<<" ";
    }
        cout<<endl;
    
}
int main()
{
    int n,m;
    cin>>n>>m;
    int output[n];
    for (int i = 0; i < n; i++)
    {
        cin>>output[i];
    }
    
    reverseArray(n,m,output);
return 0;
}