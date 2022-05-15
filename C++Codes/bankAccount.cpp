// // #include <iostream>
// // #include <string>
// // #include <cstring>
// // #include <iomanip>
// // #include <limits>
// // #include <list>
// // #include <cmath>
// // #include <vector>
// // #include <set>
// // #include <stack>
// // #include <queue>
// // #include <algorithm>
// // #include <map>
// // #include <deque>
// // #include <cstdio>

// // using namespace std;

// // int main()
// // {
// //     int n;
// //     cin >> n;
// //     if (n >= 0)
// //         cout << n;
// //     else
// //         cout << max(stoi(to_string(n).substr(0, to_string(n).length() - 1)), stoi(to_string(n).substr(0, to_string(n).length() - 2) + to_string(n).substr(to_string(n).length() - 1, 1)));
// //     return 0;
// // }

// #include <iostream>
// #include <string>
// #include <cstring>
// #include <iomanip>
// #include <limits>
// #include <list>
// #include <cmath>
// #include <vector>
// #include <set>
// #include <stack>
// #include <queue>
// #include <algorithm>
// #include <map>
// #include <deque>
// #include <cstdio>

// using namespace std;

// int main()
// {
//     long long int n, l, sl;
//     cin >> n;
//     if (n > 0)
//         cout << n;
//     else
//     {
//         l = n / 10;
//         sl = (n / 100) * 10 + (n % 10);
//         if (l >= sl)
//         {
//             cout << l;
//         }
//         else
//         {
//             cout << sl;
//         }
//     }
//     return 0;
// }

// auto t1 = high_resolution_clock::now();
//     long_operation();
//     auto t2 = high_resolution_clock::now();

//     /* Getting number of milliseconds as an integer. */
//     auto ms_int = duration_cast<milliseconds>(t2 - t1);

//     /* Getting number of milliseconds as a double. */
//     duration<double, std::milli> ms_double = t2 - t1;

#include <chrono>

/* Only needed for the sake of this example. */
#include <iostream>
#include <thread>
    
void long_operation()
{
    /* Simulating a long, heavy operation. */

    using namespace std::chrono_literals;
    std::this_thread::sleep_for(150ms);
}

int main()
{
    using std::chrono::high_resolution_clock;
    using std::chrono::duration_cast;
    using std::chrono::duration;
    using std::chrono::milliseconds;

    auto t1 = high_resolution_clock::now();
    for (int i = 0; i < 10000000000; i++)
    {
        int s = 5 + 3;
    }
    auto t2 = high_resolution_clock::now();

    
    duration<double, std::milli> ms_double = t2 - t1;

    std::cout << ms_double.count() << "ms";
    return 0;
}