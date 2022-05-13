// Use dynamic programming to find the nth fibonacci number

#include <iostream>
#include <vector>

using namespace std;

unsigned long long int fibonacci(int n, unsigned long long int arr[])
{
    if (n == 0)
    {
        return 0;
    }
    if (n == 1)
    {
        return 1;
    }
    if (arr[n] != 0)
    {
        return arr[n];
    }
    arr[n] = fibonacci(n - 1, arr) + fibonacci(n - 2, arr);
}

int main()
{
    int n;
    unsigned long long int arr[100];
    for (int i = 0; i < 100; i++)
    {
        arr[i] = 0;
    }
    cout << "Enter the number: ";
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cout << "The " << i << "th fibonacci number is: " << fibonacci(i, arr) << endl;
    }
    return 0;
}