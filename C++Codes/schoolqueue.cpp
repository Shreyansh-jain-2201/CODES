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
    int n, t, p, count = 0, run = 0;
    string q;
    cin >> n >> t;
    cin >> q;
    while (count != t && run <= 50)
    {
        p = 0;
        for (int i = 0; i < n; i++)
        {
            if (q.substr(i, 2) == "BG")
            {
                q[i] = 'G';
                q[i + 1] = 'B';
                i++;
            }
        }
        count++;
        run++;
    }
    cout << q << endl;

    return 0;
}