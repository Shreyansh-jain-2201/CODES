arrival_time = []
start_time = [0]
dict_arrival_time = {}
burst_time = []
waiting_time = []
completion_time = []
turnaround_time = []
process_id = []
n = int(input("Enter the number of processes: "))
for i in range(0, n):
    process = input("").split()
    process_id.append(process[0])
    burst_time.append(int(process[1]))
    arrival_time.append(int(process[2]))
    if arrival_time[i] in dict_arrival_time:
        dict_arrival_time[arrival_time[i]].append(burst_time[i])
    else:
        dict_arrival_time[arrival_time[i]] = [burst_time[i]]
arrival_time.sort()
p = 0
for i in range(0, n):
    if len(dict_arrival_time[arrival_time[i]]) == 1:
        burst_time[i] = int(dict_arrival_time[arrival_time[i]][0])
    else:
        burst_time[i] = int(dict_arrival_time[arrival_time[i]][p])
        p+=1
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
print(arrival_time)
print(completion_time)