#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int k;
        cin >> k;
        int a1, a2, a3, b1, b2, b3, c1, c2, c3;
        cin >> a1 >> a2 >> a3;
        cin >> b1 >> b2 >> b3;
        cin >> c1 >> c2 >> c3;
        int sum = a2 + a3 + b1 + b3 + c1 + c2;
        cout << sum / 2 << endl;
    }
    return 0;
}