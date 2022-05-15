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

void removeDuplicates(char s[])
{
    if (s[0] == '\0')
    {
        return;
    }
    if (s[0] == s[1])
    {
        removeDuplicates(s + 1);
    }
    else
    {
        cout << s[0];
        removeDuplicates(s + 1);
    }
}

void replace(char s[])
{
    if (s[0] == '\0')
    {
        return;
    }
    if (s[0] == 'a')
    {
        cout << 'x';
        replace(s + 1);
    }
    else
    {
        cout << s[0];
        replace(s + 1);
    }
}
void remove(char s[])
{
    if (s[0] == '\0')
    {
        return;
    }
    if (s[0] == 'a')
    {
        remove(s + 1);
    }
    else
    {
        cout << s[0];
        remove(s + 1);
    }
}
int length(char s[])
{
    if (s[0] == '\0')
    {
        return 0;
    }
    return 1 + length(s + 1);
}

int main()
{
    char s[100];
    cin >> s;
    // replace(s);
    // cout << endl
    //      << endl;
    removeDuplicates(s);
    return 0;
}