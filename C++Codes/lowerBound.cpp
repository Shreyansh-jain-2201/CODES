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


int main()
{
    int n, q;
    vector<int> v;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int element;
        cin >> element;

        v.push_back(element);
        
    }
    cin >> q;
    for (int i = 0; i < q; i++)
    {
        int query;
        cin>>query;
        std::vector<int>::iterator low;
        low=std::lower_bound (v.begin(), v.end(), query); 
        if(v[low-v.begin()]==query)
        {
            cout<<"Yes "<<(low-v.begin()+1)<<endl;
        }
        else
        {
            cout<<"No "<<(low-v.begin()+1)<<endl;
        }
    }
    
return 0;
}