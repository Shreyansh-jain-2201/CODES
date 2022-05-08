#include <iostream>
#include <string>
#include <vector>
#include <stack>

using namespace std;

int findChar(string str, char ch)
{
    int index = 0;
    while (index < str.size())
    {
        if (str[index] == ch)
        {
            return index;
        }
        index++;
    }
    return index;
}

void reverseStr(string &str)
{
    int n = str.length();
    for (int i = 0; i < n / 2; i++)
        swap(str[i], str[n - i - 1]);
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        string s;
        cin >> s;
        int n = s.size();
        if (n == 1)
        {
            cout << "1" << endl;
            continue;
        }
        int j = findChar(s, '0');
        s = s.substr(0, j);
        reverseStr(s);
        int i = findChar(s, '1');
        s = s.substr(0, i);
        if (s.size() + 2 <= n)
        {
            cout << s.size() + 2 << endl;
        }
        else if (s.size() + 1 <= n)
        {
            cout << s.size() + 1 << endl;
        }
        else
        {
            cout << s.size() << endl;
        }
    }
}
