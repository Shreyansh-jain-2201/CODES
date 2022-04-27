#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    int largest = a[0];
    int second_largest = a[1];
    for (int i = 0; i < n; i++)
    {
        if (a[i] > largest)
        {
            second_largest = largest;
            largest = a[i];
        }
        else if (a[i] > second_largest)
        {
            second_largest = a[i];
        }
    }
    cout << second_largest << endl;
    return 0;
}