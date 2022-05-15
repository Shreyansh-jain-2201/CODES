#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
 
using namespace std;

string snake(int a){
    string output;
    for (int i = 0; i < a; i++)
    {
        output = output + "#";
    }
    return output;
}
string revFOX(int a){
    string output;
    for (int i = 0; i < a-1; i++)
    {
        output = output + ".";
    }
    return "#" + output;
}
string FOX(int a){
    string output;
    for (int i = 0; i < a-1; i++)
    {
        output = output + ".";
    }
    return output + "#";
}
void pattern(int a,int b){
    for (int i = 0; i < b/4; i++)
    {
        cout<<snake(a)<<endl;
        cout<<FOX(a)<<endl;
        cout<<snake(a)<<endl;
        cout<<revFOX(a)<<endl;
    }
    b = b%4;
    if (b == 3)
    {
        cout<<snake(a)<<endl;
        cout<<FOX(a)<<endl;
        cout<<snake(a)<<endl;
    }
    else if (b == 2)
    {
        cout<<snake(a)<<endl;
        cout<<FOX(a)<<endl;
    }
    else if (b == 1)
    {
        cout<<snake(a)<<endl;
    }
}

int main()
{
    int a,b;
    cin>>b>>a;
    pattern(a,b);
return 0;
}