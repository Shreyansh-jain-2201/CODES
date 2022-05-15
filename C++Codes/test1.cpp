// { Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution
{
public:
    int countX(int L, int R, int X)
    {
        int output = 0;
        for (int p = L; p <= R; p++)
        {
            int i = p;
            while (i > 9)
            {
                if (i % 10 == X)
                {
                    output = output + 1;
                    break;
                }
                i = i / 10;
            }
        }
        return output;
    }
};

// { Driver Code Starts.
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int L, R, X;
        cin >> L >> R >> X;
        Solution ob;
        int ans = ob.countX(L, R, X);
        cout << ans << "\n";
    }
}
// } Driver Code Ends