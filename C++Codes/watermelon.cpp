#include<iostream>

int main()
{
    int w;
    std::cin >> w;
    if(w%2 || w == 2)
    {
        std::cout << "NO";
    }
    else
    {
        std::cout << "YES";
    }
    return 0;
}