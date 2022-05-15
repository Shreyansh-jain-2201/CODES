// #include <iostream>
// #include <string>
// #include <cstring>
// #include <iomanip>
// #include <limits>
// #include <list>
// #include <cmath>
// #include <vector>
// #include <sstream>
 
// using namespace std;
 
 
// int to_int(string s){
 
// 	int output = stoi(s);
//     return output;
// }
// int sum(string s){
//     int sum = 0;
//     for (int i = 0; i < s.length(); i++)
//     {
//         sum=sum + to_int(s.substr(i,1));
//     }
//     return sum;
    
// }
// string largestNUM(int n, int s){
//     string output;
//     int a = n;
//     int b = s;
//     int t;
//     if (n == 1 && s == 0)
//     {
//         return "0";
//     }
//     else if (n != 1 && s == 0)
//     {
//         return "-1";
//     }
//     while(s>=9){
//         s = s - 9;
//         output = output + '9';
//     }
//     if (s)
//     {
//         output = output + to_string(s);
//     }
//     t = n - output.length();
//     for (int i = 0; i < t; i++)
//     {
//         output = output + '0';
//     }
//     if (output.length() == a && sum(output) == b)
//     {
//         return output;
//     }
//     else{
//         return "-1";
//     }
//     if(output.substr(0,1) == "0" || output.length() != a){
//         return "-1";
//     }
//     return output;
    
    
// }
// // string smallestNUM(int n, int s){
// //     int a = n;
// //     int b = s;
// //     string output, str;
// //     string num = largestNUM(n,s).substr(n-1,1);
// //     if (n == 1 && s == 0)
// //     {
// //         return "0";
// //     }
// //     if(num == "0"){
// //         s = s-1;
// //         n = n-1;
// //         output = output + "1";
// //     }
// //     str = largestNUM(n,s);
// //     if (largestNUM(n,s) == "-1")
// //     {
// //         return "-1";
// //     }
    
// //     for (int i = 0; i < n / 2; i++)
// //         {swap(str[i], str[n - i - 1]);}
// //     output = output + str;
// //     if (output.length() == a && sum(output) == b)
// //     {
// //         return output;
// //     }
// //     else{
// //         return "-1";
// //     }
// // }

// string smallestNUM(int n, int s)
// {
//     string output, number;
//     int t;
//     int a = n;
//     if ((n-1) * 9 >= s)
//     {
//         output = output + "1";
//         n = n-1;
//         s = s-1;
//     }
    
//     while(s>=9){
//         s = s - 9;
//         number = number + '9';
//     }
//     if (s)
//     {
//         number = number + to_string(s);
//     }
//     t = a - output.length();
//     for (int i = 0; i < t; i++)
//     {
//         output = output + '0';
//     }
    
//     for (int i = 0; i < number.length() / 2; i++)
//         {swap(number[i], number[number.length() - i - 1]);}

//     output = output + number;
//     output = to_string(to_int(output));
//     if(output.substr(0,1) == "0" || output.length() != a){
//         return "-1";
//     }
//     return output;
// }
// int main()
// {
//     int n,s;
//     cin>>n>>s;
//     cout<<smallestNUM(n,s)<<" ";
//     cout<<largestNUM(n,s);
// return 0;
// }

#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <limits>
#include <list>
#include <cmath>
#include <vector>
#include <sstream>
 
using namespace std;
 
 
int to_int(string s){
 
	int output = stoi(s);
    return output;
}
int sum(string s){
    int sum = 0;
    for (int i = 0; i < s.length(); i++)
    {
        sum=sum + to_int(s.substr(i,1));
    }
    return sum;
    
}
string largestNUM(int n, int s){
    string output;
    int a = n;
    int b = s;
    int t;
    if (n == 1 && s == 0)
    {
        return "0";
    }
    while(s>=9){
        s = s - 9;
        output = output + '9';
    }
    if (s)
    {
        output = output + to_string(s);
    }
    t = n - output.length();
    for (int i = 0; i < t; i++)
    {
        output = output + '0';
    }
    // if (output.length() == a && sum(output) == b)
    // {
    //     return output;
    // }
    // else{
    //     return "-1";
    // }
    if(output.substr(0,1) == "0" || output.length() != a){
        return "-1";
    }
    return output;
    
    
}
string smallestNUM(int n, int s){
    int a = n;
    int b = s;
    string output, str;
    string num = largestNUM(n,s).substr(n-1,1);
    if (n == 1 && s == 0)
    {
        return "0";
    }
    if(num == "0"){
        s = s-1;
        n = n-1;
        output = output + "1";
    }
    str = largestNUM(n,s);
    if (largestNUM(n,s) == "-1")
    {
        return "-1";
    }
    
    for (int i = 0; i < n / 2; i++)
        {swap(str[i], str[n - i - 1]);}
    output = output + str;
    if (output.length() == a && sum(output) == b)
    {
        return output;
    }
    else{
        return "-1";
    }
}
int main()
{
    int n,s;
    cin>>n>>s;
    cout<<smallestNUM(n,s)<<" ";
    cout<<largestNUM(n,s);
    // cout<<(to_int("2456") - 6);
    // cout<<endl<<sum(largestNUM(n,s));
return 0;
}