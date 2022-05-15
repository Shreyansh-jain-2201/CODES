def bubbleSort(arr):
    for i in range(len(arr)):
        flag = 0
        for j in range(len(arr) - i):
            try:
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
                    flag = 1
            except:
                continue
    return arr


def sum(array):
    sum = 0
    for i in array:
        sum += i
    return sum


def ZeroMatrix(array):
    sum = 0
    for i in array:
        sum += i
    if sum == 0:
        return True
    else:
        return False
    

def shortest(array):
    s = 0
    index = 0
    if ZeroMatrix(array):
        return -1
    for i in array:
        if i:
            s = i
            break
    for i in range(len(array)):
        if array[i] < s:
            s = array[i]
            index = i
    return index
    
arrival_time = []
burst_time = []
gantt_chart = []
clock = 0
# n = int(input("Enter the number of processes: "))
n = int(input(""))
for i in range(0, n):
    # arrival_time.append(int(input(f"Enter the burst time of process P{str(i+1)}: ")))
    arrival_time.append(int(input("")))
    # burst_time.append(int(input(f"Enter the arrival time of process P{str(i+1)}: ")))
    burst_time.append(int(input("")))
num = sum(burst_time)
print(num)
# while num >= len(gantt_chart):
#     i = 0
#     p = 0
#     if arrival_time[shortest(burst_time, i)] <= clock and shortest(burst_time, i) != -1:
#         clock += 1
#         burst_time[shortest(burst_time,i)] = burst_time[shortest(burst_time,i)] - 1
#         gantt_chart.append(shortest(burst_time,i))
#     else:
#         while not p:
#             i += 1
#             if arrival_time[shortest(burst_time,i)] <= clock and shortest(burst_time,i) != -1:
#                 clock += 1
#                 burst_time[shortest(burst_time,i)] = burst_time[shortest(burst_time,i)] - 1
#                 gantt_chart.append(shortest(burst_time,i))
#                 p = 1
#     print(gantt_chart)
#     print(len(gantt_chart))






for j in range(num + 1):
    if ZeroMatrix(burst_time):
        break
    for k in range(num+1):
        if ZeroMatrix(burst_time):
            break
        burst_time_new = []
        for i in range(len(arrival_time)):
            if arrival_time[i] <= clock:
                burst_time_new.append(burst_time[i])
        if burst_time[burst_time.index(burst_time_new[shortest(burst_time_new)])] > 0:
            gantt_chart.append(burst_time.index(burst_time_new[shortest(burst_time_new)]))
            burst_time[burst_time.index(burst_time_new[shortest(burst_time_new)])] -= 1
        clock += 1
print(gantt_chart)
    




# for j in range(num):
#     if ZeroMatrix(burst_time):
#         break
#     for i in range(num):
#         if ZeroMatrix(burst_time):
#             break
#         if arrival_time[shortest(burst_time, i)] <= clock and burst_time[shortest(burst_time, i)] > 0:
#             # print(shortest(burst_time, i))
#             print(i)
#             # print("break")
#             gantt_chart.append(shortest(burst_time, i))
#             burst_time[shortest(burst_time, i)] = burst_time[shortest(burst_time, i)] - 1
#             clock += 1
#             break
        


print(len(gantt_chart))
print(gantt_chart)
print(burst_time)









# 5
# 2
# 6
# 5
# 2
# 1
# 8
# 0
# 3
# 4
# 4