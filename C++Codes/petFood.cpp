#include <iostream>
#include <string>

using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int a, b, c, x, y;
        cin >> a >> b >> c >> x >> y;
        int remainingCats = x - a;
        int remainingDogs = y - b;
        if (remainingCats <= 0)
        {
            remainingCats = 0;
        }
        if (remainingDogs <= 0)
        {
            remainingDogs = 0;
        }
        int remainingFood = c;
        if (remainingCats + remainingDogs <= remainingFood)
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }
    return 0;
}
