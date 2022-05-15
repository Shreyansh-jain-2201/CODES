#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <map>
#include <deque>
#include <cstdio>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int n;
        cin >> n;
        string s1;
        string s2;
        cin >> s1;
        cin >> s2;
        string output = "";

        while (s1.length() > 0 || s2.length() > 0)
        {
            if (s1.substr(0, 1) == "0")
            {
                output = output + s1.substr(0, 1);
                s1.erase(0, 1);
                cout << "A" << endl;
            }
            else if (s2.substr(0, 1) == "0")
            {
                cout << "B" << endl;
                output = output + s1.substr(0, 1);
                s2.erase(0, 1);
            }
            else
            {
                cout << "C" << endl;
                int n1 = 0;
                int n2 = 0;
                for (int k = 0; k < s1.length(); k++)
                {
                    if (s1.substr(k, 1) == "0")
                    {
                        cout << "D" << endl;
                        cout << k << endl;
                        cout << s1 << endl;
                        n1 = k;
                        break;
                    }
                }
                for (int k = 0; k < s2.length(); k++)
                {
                    cout << "P" << k << endl
                         << s2 << endl;
                    if (s2.substr(k, 1) == "0")
                    {
                        cout << "E" << endl;
                        n2 = k;
                        break;
                    }
                }
                if (n1 == 0)
                {
                    output = output + s2 + s1;
                    s1.erase();
                    s2.erase();
                    break;
                }
                else if (n2 == 0)
                {
                    output = output + s1 + s2;
                    s1.erase();
                    s2.erase();
                    break;
                }
                if (n1 < n2)
                {
                    cout << "F" << endl;
                    output = output + s1.substr(0, n1);
                    s1.erase(0, n1);
                }
                else
                {
                    cout << "G" << endl;
                    output = output + s2.substr(0, n2);
                    s2.erase(0, n2);
                }
            }
        }
        cout << output << endl;
    }
    cout << endl;

    return 0;
}