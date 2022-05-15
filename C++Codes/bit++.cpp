
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
    int n;
    string op;
    float x = 0;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        string o;
        cin >> o;
        op = op + o;
    }
    for (int i = 0; i < op.length(); i++)
    {
        if (op[i] == '-')
        {
            x = x - 0.5;
        }
        else if (op[i] == '+')
        {
            x = x + 0.5;
        }
        else{
            continue;
        }
        
    }
    cout<<x<<endl;
    return 0;
}