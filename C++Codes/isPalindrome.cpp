#include<iostream>
#include<string>
#include<math.h>
using namespace std;

bool isPalindrome(int n)
{
    int q = n;
    string s = to_string(q);
    string t;
    int p;
    while(n!=0)
    {
        p = n%10;
        n = n/10;
        cout<<p<<endl;
        t+= to_string(p);
    }

    cout<<t<<endl;
    if(s == t)
    {
        return true;
    }
    return false;
}

int main()
{
    int n;
    cin>>n;
    if(isPalindrome(n))
    {
        cout<<"true";
    }
    else
    {
        cout<<"false";
    }
    return 0;
}