// KMP first code

#include <iostream>
#include <algorithm>
using namespace std;

int kmp(string text, string pattern)
{

    if (text.size() == 0 || pattern.size() == 0)
        return -1;

    int failure[pattern.size()];
    std::fill(failure, failure + pattern.size(), -1);

    for (int r = 1, l = -1; r < pattern.size(); r++)
    {

        while (l != -1 && pattern[l + 1] != pattern[r])
            l = failure[l];

        if (pattern[l + 1] == pattern[r])
            failure[r] = ++l;
    }

    int tail = -1;
    for (int i = 0; i < text.size(); i++)
    {

        while (tail != -1 && text[i] != pattern[tail + 1])
            tail = failure[tail];

        if (text[i] == pattern[tail + 1])
            tail++;

        if (tail == pattern.size() - 1)
            return i - tail;
    }

    return -1;
}

int main()
{
    string text;
    string pattern;
    cout << endl
         << endl
         << endl
         << endl
         << "Enter the text: ";
    cin >> text;
    cout << "Enter the pattern: ";
    cin >> pattern;
    if (kmp(text, pattern) == -1)
    {
        cout << "The pattern does not occur in the given text.";
    }
    else
    {
        cout << "The pattern occurs at shift " << kmp(text, pattern);
    }
    cout << endl
         << endl
         << endl
         << endl;
    return 0;
}
