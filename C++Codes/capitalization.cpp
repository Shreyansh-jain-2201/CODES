#include <iostream>
#include <string.h>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include<algorithm>
#include <vector>
 
using namespace std;
int main()
{
    string s;
    cin>>s;
    string s1 = s.substr(0,1);
    string s2 = s.substr(1, s.length()-1);
    transform(s1.begin(), s1.end(), s1.begin(), ::toupper);
    s = s1 + s2;
    cout<<s;
return 0;
}