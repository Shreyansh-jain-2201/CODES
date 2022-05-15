temp1 = []
clock = 0
burst_time = []
start_time = [0]
dict_burst_time = {}
arrival_time = []
waiting_time = []
completion_time = []
turnaround_time = []
n = int(input("Enter the number of processes: "))
for i in range(0, n):
    arrival_time.append(int(input(f"Enter the burst time of process P{str(i+1)}: ")))
    burst_time.append(int(input(f"Enter the arrival time of process P{str(i+1)}: ")))
    if burst_time[i] in dict_burst_time:
        dict_burst_time[burst_time[i]].append(arrival_time[i])
    else:
        dict_burst_time[burst_time[i]] = [arrival_time[i]]
burst_time.sort()
p = 0
for i in range(0, n):
    if len(dict_burst_time[burst_time[i]]) == 1:
        arrival_time[i] = int(dict_burst_time[burst_time[i]][0])
    else:
        arrival_time[i] = int(dict_burst_time[burst_time[i]][p])
        p+=1
p = 1
for j in range(0, n):
    for i in range(0, n):
        if arrival_time[i] <= clock and i not in temp1:
            temp1.append(i)
            clock += burst_time[i]
            p = 0
            break
    if p:
        clock += 1
new_arrival_time = arrival_time
new_burst_time = burst_time
arrival_time = []
burst_time = []
for i in temp1:
    arrival_time.append(new_arrival_time[i])
    burst_time.append(new_burst_time[i])

for i in range(n):
    if i>0:
        start_time.append(burst_time[i-1] + start_time[i-1])
    if start_time[i]<arrival_time[i]:
        start_time[i] = arrival_time[i]
    completion_time.append(start_time[i] + burst_time[i])
    turnaround_time.append(completion_time[i] - arrival_time[i])
    waiting_time.append(turnaround_time[i] - burst_time[i])
total_turnaround_time = 0
total_waiting_time = 0
for i in range(0, n):
    total_turnaround_time += turnaround_time[i]
    total_waiting_time += waiting_time[i]
print(f"The average waiting time is {total_waiting_time/n} ms.")
print(f"The average turnaround time is {total_turnaround_time/n} ms.")