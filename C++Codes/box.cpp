#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
 
using namespace std;

class Box
{
private:
    int l;
    int b;
    int h;
public:
    Box()
    {
        this->l = 0;
        this->b = 0;
        this->h = 0;
    }
    Box(const Box &B2)
    {
        this->l = B2.l;
        this->b = B2.b;
        this->h = B2.h;
    }
    Box(int length, int breadth, int height)
    {
        this->l = length;
        this->b = breadth;
        this->h = height;
    }
    int getLength()
    {
        return this->l;
    }
    int getBreadth()
    {
        return this->b;
    }
    int getHeight()
    {
        return this->h;
    }
    long long CalculateVolume()
    {
        return (long long) (this->l) * (this->b) * (this->h);
    }
    bool operator< (Box &B)
    {
        if((this->l < B.l) || (this->b < B.b && this->l == B.l)|| (this->h < B.h && this->l == B.l && this->b == B.b))
        {
            return true;
        }
        else
        {
            return false;
        }
    }

};
ostream& operator<<(ostream& out,Box& B)
{
    out<<B.getLength()<<" "<<B.getBreadth()<<" "<<B.getHeight();
    return out;
};

void check2()
{
	int n;
	cin>>n;
	Box temp;
	for(int i=0;i<n;i++)
	{
		int type;
		cin>>type;
		if(type ==1)
		{
			cout<<temp<<endl;
		}
		if(type == 2)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			temp=NewBox;
			cout<<temp<<endl;
		}
		if(type==3)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			if(NewBox<temp)
			{
				cout<<"Lesser\n";
			}
			else
			{
				cout<<"Greater\n";
			}
		}
		if(type==4)
		{
			cout<<temp.CalculateVolume()<<endl;
		}
		if(type==5)
		{
			Box NewBox(temp);
			cout<<NewBox<<endl;
		}

	}
}
 
 
int main()
{
    check2();
return 0;
}