#include <cstdio>
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
#include <deque>
#include <queue>
#include <algorithm>
#include <map>

using namespace std;


int main()
{
    map<string, int> m;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int action;
        cin>>action;
        string x;
        cin >> x;
        if (action == 1)
        {
            int y;
            cin >> y;
            map<string, int> :: iterator itr =m.find(x);
            if (itr == m.end())
            {
                m.insert(make_pair(x, y));
            }
            else
            {
                itr->second = itr->second + y;
            }

        }
        else if (action == 2)
        {
            m.erase(x);
        }
        else if (action == 3)
        {
            map<string, int> :: iterator itr =m.find(x);
            if (itr == m.end())
            {
                cout << "0" << endl;
            }
            else
            {
                cout << itr->second << endl;
                
            }
        }
    }
return 0;
}