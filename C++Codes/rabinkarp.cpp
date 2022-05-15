// Rabin karp 2
#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

void rabinKarp(string text, string pattern)
{
    if (text.length() && pattern.length())
    {
        int n = text.length();
        int m = pattern.length();
        int i, j;           // iterators for loops
        int s = 0, p = 0;   // s = hash of string, p = hash of pattern
        const int pm = 256; // no of characters in alphabet
        const int q = 101;  // large prime number
        int h = 1;          // h = multiplier for MSB
        bool flag = false;

        for (i = 0; i < m - 1; i++)
            h = (h * pm) % q;

        for (i = 0; i < m; i++)
        {
            s = (pm * s + text[i]) % q;
            p = (pm * p + pattern[i]) % q;
        }

        for (i = 0; i <= n - m; i++)
        {
            if (s == p)
            {
                for (j = 0; j < m; j++)
                    if (text[i + j] != pattern[j])
                        break;
                if (j == m)
                {
                    cout << "Pattern found at shift " << i + 1 << endl;
                    flag = true;
                }
            }

            s = (pm * (s - h * text[i]) + text[i + m]) % q;
            if (s < 0) // still dont know why we do this :|
                s = s + q;
        }
        if (!flag)
            cout << "The pattern does not occur in the given text." << endl;
        return;
    }
    cout << "Text or pattern cannot be empty.." << endl;
    return;
}

int main()
{
    string text;
    string pattern;
    cout << "Enter the text: ";
    cin >> text;
    cout << "Enter the pattern: ";
    cin >> pattern;
    rabinKarp(text, pattern);

    return 0;
}