#include<iostream>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int i = 0; i<t; i++)
    {
        int n,x;
        cin>>n>>x;
        cout<<(x%(n+1))<<endl;
    }
}