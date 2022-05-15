#include <iostream>
#include<set>
#include<string>
 
using namespace std;

void lucky(int n){
    set<int>s;
    s.insert(7);
    s.insert(4);
    set<int>y;
    set<int> :: iterator it;
    string str;
    
    for (int i = 0; i < n; i++)
    {
        str = to_string(i);
        for (int j = 0; j < str.length(); j++)
        {
            y.insert(int(str[j]));
        }
        
        for (it = y.begin(); it != y.end(); it++)
        {
            cout<<*it<<endl;
        }
        y.clear();
    }
    
}

int main()
{
    lucky(50);
return 0;
}