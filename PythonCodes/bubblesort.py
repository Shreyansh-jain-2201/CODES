# #include <iostream>
# #include <string>
# #include <cstring>
# #include <iomanip>
# #include <limits>
# #include <list>
# #include <cmath>
# #include <vector>

# using namespace std;

# int main()
# {
#     int n;
#     cin>>n;
#     int arr[n];
#     for (int i = 0; i < n; i++)
#     {
#         cin>>arr[i];
#     }
#     for (int i = 0; i < n; i++)
#     {
#         int flag = 0;
#         for (int j = 0; j < n-i-1; j++)
#         {
#             int temp;
#             if (arr[j] > arr[j+1])
#             {
#                 temp = arr[j];
#                 arr[j] = arr[j+1];
#                 arr[j+1] = temp;
#                 flag = 1;
#             }
#         }
#         if (flag == 0)
#         {
#             break;
#         }
#     }
#     for (int i = 0; i < n; i++)
#     {
#         cout<<arr[i]<<" ";
#     }
# return 0;
# }

f = int(input())


def ftoc(f):
    return ((f-32)*5.0)/9.0


output = str(ftoc(f))
try:
    print(output[0:output.index(".")+3])
except:
    print(output)
