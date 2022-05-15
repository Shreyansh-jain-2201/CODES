#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>

using namespace std;

void revArray(int output[], int n)
{
    int temp;
    for (int i = 0; i < n / 2; i++)
    {
        temp = output[i];
        output[i] = output[n-1-i];
        output[n-1-i] = temp;
    }
    for (int i = 0; i < n; i++)
    {
        cout<<output[i]<<" ";
    }
    
}
int main()
{
    int n, output[n];
    cin>>n;
    for (int i = 0; i < n; i++)
    {
        cin>>output[i];
    }
    revArray(output, n);
    return 0;
}