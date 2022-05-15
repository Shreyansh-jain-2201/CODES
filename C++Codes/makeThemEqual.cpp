#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int n;
        cin >> n;
        int arr[n];
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }
        int smallest = arr[0];
        int largest = arr[0];
        for (int i = 0; i < n; i++)
        {
            if (arr[i] > largest)
            {
                largest = arr[i];
            }
            if (arr[i] < smallest)
            {
                smallest = arr[i];
            }
        }
        cout << largest - smallest << endl;
    }

    return 0;
}