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

int lexi(unsigned string word)
{
    string s;
    s = "abcdeghijklmnopqrstuvwxyz";
    /*transform(word.begin(), word.end(), word.begin(), ::tolower);*/
    int found = s.find('f');
    return found;

}
int main()
{
    unsigned string s = "hello";
    cout<<lexi(s);
return 0;
}