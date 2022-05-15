#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>


using namespace std;
void bubbleSort(int arr[4])
{
   int i, j, n = 4;
   bool swapped;
   for (i = 0; i < n-1; i++)
   {
     swapped = false;
     for (j = 0; j < n-i-1; j++)
     {
        if (arr[j] > arr[j+1])
        {
           swap(&arr[j], &arr[j+1]);
           swapped = true;
        }
int main()
{
    int a,b,c,d,e,f,g;
    cin>>d>>e>>f>>g;
    bubbleSort([d,e,f,g])
    a = e + d - g;
    b = e + f - g;
    c = d + f - g;
    cout<<a<<" ";
    cout<<b<<" ";
    cout<<c<<" ";
return 0;
}