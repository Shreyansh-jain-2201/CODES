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
    int n,k,d;
    int count = 0;
    cin>>n>>k;
    int scores[n];
    for (int i = 0; i < n; i++)
    {
        int score;
        cin>>score;
        scores[i] = score;
    }
    d = scores[k-1];
    for (int i = 0; i < n; i++)
    {
        if (scores[i]>=d && scores[i]>0)
        {
            count++;
        }
        
    }
    cout<<count<<endl;
    
    
return 0;
}