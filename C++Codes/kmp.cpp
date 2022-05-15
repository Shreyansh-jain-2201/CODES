// KMP second code
#include <iostream>
#include <string>

using namespace std;

int *pre_kmp(string pattern)
{
    int size = pattern.size();
    int *pie = new int[size];
    pie[0] = 0;
    int k = 0;
    for (int i = 1; i < size; i++)
    {
        while (k > 0 && pattern[k] != pattern[i])
        {
            k = pie[k - 1];
        }
        if (pattern[k] == pattern[i])
        {
            k = k + 1;
        }
        pie[i] = k;
    }

    return pie;
}

void kmp(string text, string pattern)
{
    int *pie = pre_kmp(pattern);
    int temp = 0;
    int matched_pos = 0;
    for (int current = 0; current < text.length(); current++)
    {
        while (matched_pos > 0 && pattern[matched_pos] != text[current])
            matched_pos = pie[matched_pos - 1];

        if (pattern[matched_pos] == text[current])
            matched_pos = matched_pos + 1;

        if (matched_pos == (pattern.length()))
        {
            cout << "Pattern occurs with shift " << current - (pattern.length() - 1);
            temp++;
            matched_pos = pie[matched_pos - 1];
        }
    }
    if (temp == 0)
    {

        cout << "Pattern not found! ";
    }
}
int main()
{
    cout << "________Knuth-Morris_Pratt________" << endl;
    string text, pattern;
    cout << "Enter the text: ";
    cin >> text;
    cout << "Enter pattern: ";
    cin >> pattern;

    kmp(text, pattern);

    return 0;
}