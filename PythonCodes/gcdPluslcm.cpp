#include <iostream>

using namespace std;

int gcd(int a, int b)
{
    if (b == 0)
    {
        return a;
    }
    return gcd(b, a % b);
}

int lcm(int a, int b)
{
    return (a * b) / gcd(a, b);
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        int p = 0;
        for (int i = 1; i < n; i++)
        {
            for (int j = 1; j <= n - i; j++)
            {
                for (int k = 1; k <= n - i - j; k++)
                {
                    int l = n - i - j - k;
                    if (gcd(i, j) == lcm(k, l))
                    {
                        cout << i << " " << j << " " << k << " " << l << endl;
                        p++;
                        break;
                    }
                    else if (gcd(i, k) == lcm(j, l))
                    {
                        cout << i << " " << k << " " << j << " " << l << endl;
                        p++;
                        break;
                    }
                    else if (gcd(i, l) == lcm(j, k))
                    {
                        cout << i << " " << l << " " << j << " " << k << endl;
                        p++;
                        break;
                    }
                    else if (gcd(j, k) == lcm(i, l))
                    {
                        cout << j << " " << k << " " << i << " " << l << endl;
                        p++;
                        break;
                    }
                    else if (gcd(j, l) == lcm(i, k))
                    {
                        cout << j << " " << l << " " << i << " " << k << endl;
                        p++;
                        break;
                    }
                    else if (gcd(k, l) == lcm(i, j))
                    {
                        cout << k << " " << l << " " << i << " " << j << endl;
                        p++;
                        break;
                    }
                    if (p > 0)
                    {
                        break;
                    }
                }
                if (p > 0)
                {
                    break;
                }
            }
            if (p > 0)
            {
                break;
            }
        }
    }
}