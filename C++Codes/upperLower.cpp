#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <algorithm>
#include <ctype.h>

using namespace std;
int main()
{
    int i = 0, lower = 0, upper = 0;
    char str[100];
    cin >> str;
    char c;
    while (str[i])
    {
        c = str[i];
        if (islower(c))
        {
            lower++;
        }
        else
        {
            upper++;
        }
        i++;
    }
    string word = str;
    if (upper > lower)
    {
        transform(word.begin(), word.end(), word.begin(), ::toupper);
    }
    else
    {
        transform(word.begin(), word.end(), word.begin(), ::tolower);
    }
    cout<<word<<endl;

    return 0;
}