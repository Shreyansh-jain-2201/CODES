#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    for (int i = 0; i <= n; i++)
    {

        int weeks, days;
        weeks = i / 7;
        days = i % 7;
        if (days && weeks)
        {
            if (days == 1 && weeks == 1)
            {
                cout << weeks << " week + " << days << " day" << endl;
            }
            else if (days == 1)
            {
                cout << weeks << " weeks + " << days << " day" << endl;
            }
            else if (weeks == 1)
            {
                cout << weeks << " week + " << days << " days" << endl;
            }
            else
            {
                cout << weeks << " weeks + " << days << " days" << endl;
            }
        }
        else if (weeks)
        {
            if (weeks == 1)
            {
                cout << weeks << " week" << endl;
            }
            else
            {
                cout << weeks << " weeks" << endl;
            }
        }
        else
        {
            if (days == 1)
            {
                cout << days << " day" << endl;
            }
            else
            {
                cout << days << " days" << endl;
            }
        }
    }
    return 0;
}