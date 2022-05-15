#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
#include<algorithm>
 
using namespace std;

long string magic(long string word){
    long string output;
    transform(word.begin(), word.end(), word.begin(), ::tolower);
    for (int i = 0; i < word.length(); i++)
    {
        if (word[i] == 'a' || word[i] == 'e' || word[i] == 'i' || word[i] == 'o' || word[i] == 'u' || word[i] == 'y')
        {
            continue;
        }
        else
        {
            output = output + '.' + word[i];
        }
    }
    return output;
}
int main()
{
    long string s;
    cin>>s;
    cout<<magic(s);
return 0;
}