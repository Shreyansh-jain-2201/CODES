#include<iostream>
#include<string>
using namespace std;
int main()
{
    string s1,s2;
    int c1,c2,f=0;
    getline(cin,s1);
    getline(cin,s2);
    for(int i=0;i<s1.length();i++)
    {
        s1[i]=tolower(s1[i]);
        s2[i]=tolower(s2[i]);
    }
    for(int i=0;i<s1.length();i++)
    {
        if(s1[i]!=s2[i])
        {
            if(int(s1[i]>s2[i]))
            {
            cout<<"1";
            f=1;
            break;
            }
            if(int(s2[i])>int(s1[i]))
            {
            cout<<"-1";
            f=1;
            break;
            }
        }
    }
    if(f==0)
    cout<<"0";
    return 0;

}