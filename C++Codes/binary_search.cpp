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
    for (int i = 0; i < n; i++) {
        cin>>arr[i];
    }
    int key;
    cin>>key;
    int s = 0, e = n-1, p = 1,mid = (s+e)/2;
    while (p && s < e){
        mid = (s+e)/2;
        if(arr[mid] == key)
        {
            p = 0;
            cout<<"Key fount at position "<<mid + 1<<"."<<endl;
        }
        else if(arr[mid] > key){
            e = mid -1;
        }
        else
        {
            s = mid + 1;
        }
    }
    if(p)
    cout<<"Key not found!!";
return 0;
}