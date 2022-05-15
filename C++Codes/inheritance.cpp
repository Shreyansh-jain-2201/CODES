#include <iostream>

using namespace std;

class Triangle
{
    public:
        void triangle()
        {
            cout<<"I am a triangle\n";
        }
};

class Isosceles : public Triangle{
    public:
        void isosceles()
        {
            cout<<"I am an isosceles triangle\nI am a triangle\n";
        }
};

class Equilateral : public Isosceles
{
    public:
    void equilateral()
    {
        cout<<"I am an equilateral triangle\n";
        isosceles();
    }
};
int main()
{
    Equilateral eq;
    eq.equilateral();
return 0;
}