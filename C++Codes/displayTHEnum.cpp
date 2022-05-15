#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
 
using namespace std;
string maxNUM(int n) {
    string number = to_string(n);
    string output;
    if (number[number.length()-1] == '0' || number[number.length()-1] == '2' || number[number.length()-1] == '4' || number[number.length()-1] == '6' || number[number.length()-1] == '8'){
        n = n/2;
    }
    else
    {
        n = (n - 3)/2;
        output = output + '7';
    }
    for (int i = 0; i < n; i++){
        output = output + '1';
    }
    return output;
}
 
int main()
{
    int t;
    cin>>t;
    for(int i = 0; i < t; i++){
        int n;
        cin>>n;
        cout<<maxNUM(n)<<endl;;
    }
return 0;
}