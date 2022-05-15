#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <algorithm>
#include <cmath>
#include <vector>
 
using namespace std;

 
int main()
{
    vector<int> v;
    int n;
    cin>>n;
    for(int i=0; i<n;i++)
    {
        int element;
        cin>>element;
        v.push_back(element);
    }
    int x, a, b;
    cin>>x;
    v.erase(v.begin()+x-1);
    cin>>a>>b;
    v.erase(v.begin()+ a-1, v.begin() + b-1);
    cout<<v.size()<<endl;
    for(int i=0; i<v.size(); i++)
    {
        cout<<v.at(i)<<" ";
    }
    cout<<endl;
return 0;
}