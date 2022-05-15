#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
#include <iostream>

using namespace std;
int main()
{
    int n;
    cin >> n;
    if (n % 5 != 0)
    {
        cout << n / 5 + 1 << endl;
    }
    else
    {
        cout << n / 5 << endl;
    }

    return 0;
}
