#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
 
using namespace std;

class students
{
private:
    /* data */
public:
    int scores[5];
    void input(int a, int b, int c, int d, int e)
    {
        scores[0] = a;
        scores[1] = b;
        scores[2] = c;
        scores[3] = d;
        scores[4] = e;
    }
    int calculateTotalScore()
    {
        int sum = 0;
        for (int i = 0; i < 5; i++)
        {
            sum = sum + scores[i];
        }
        return sum;
        
    }
};

int main()
{
    int num = 0;
    int n;
    cin>>n;
    students s[n];
    for (int i = 0; i < n; i++)
    {
        int a,b,c,d,e;
        cin>>a>>b>>c>>d>>e;
        s[i].input(a,b,c,d,e);
    }
    int kristenscore = s[0].calculateTotalScore();
    for (int i = 1; i < n; i++)
    {
        if (s[i].calculateTotalScore() > kristenscore)
        {
            num ++;
        }
        
    }
    cout<<num;
return 0;
}