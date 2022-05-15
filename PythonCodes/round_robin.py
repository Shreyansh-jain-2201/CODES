

class RoundRobin:

    def collect_info(self, total_no_of_processes):
        info = []
        for i in range(total_no_of_processes):
            temporary = []
            process_id = int(input("Enter Process ID: "))
            arrival_time = int(
                input(f"Enter Arrival Time for Process {process_id}: "))
            burst_time = int(
                input(f"Enter Burst Time for Process {process_id}: "))
            temporary.extend(
                [process_id, arrival_time, burst_time, 0, burst_time])
            info.append(temporary)
        time_slice = int(input("Enter Time Slice: "))
        RoundRobin.schedulingProcess(self, info, time_slice)

    def schedulingProcess(self, info, time_slice):
        start_time = []
        exit_time = []
        executed_process = []
        ready_queue = []
        s_time = 0
        info.sort(key=lambda x: x[1])
        while 1:
            normal_queue = []
            temp = []
            for i in range(len(info)):
                if info[i][1] <= s_time and info[i][3] == 0:
                    present = 0
                    if len(ready_queue) != 0:
                        for k in range(len(ready_queue)):
                            if info[i][0] == ready_queue[k][0]:
                                present = 1
                    if present == 0:
                        temp.extend([info[i][0], info[i][1],
                                    info[i][2], info[i][4]])
                        ready_queue.append(temp)
                        temp = []
                    if len(ready_queue) != 0 and len(executed_process) != 0:
                        for k in range(len(ready_queue)):
                            if ready_queue[k][0] == executed_process[len(executed_process) - 1]:
                                ready_queue.insert(
                                    (len(ready_queue) - 1), ready_queue.pop(k))
                elif info[i][3] == 0:
                    temp.extend([info[i][0], info[i][1],
                                info[i][2], info[i][4]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break
            if len(ready_queue) != 0:
                if ready_queue[0][2] > time_slice:
                    start_time.append(s_time)
                    s_time = s_time + time_slice
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(info)):
                        if info[j][0] == ready_queue[0][0]:
                            break
                    info[j][2] = info[j][2] - time_slice
                    ready_queue.pop(0)
                elif ready_queue[0][2] <= time_slice:
                    start_time.append(s_time)
                    s_time = s_time + ready_queue[0][2]
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(info)):
                        if info[j][0] == ready_queue[0][0]:
                            break
                    info[j][2] = 0
                    info[j][3] = 1
                    info[j].append(e_time)
                    ready_queue.pop(0)
            elif len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                if normal_queue[0][2] > time_slice:
                    start_time.append(s_time)
                    s_time = s_time + time_slice
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(normal_queue[0][0])
                    for j in range(len(info)):
                        if info[j][0] == normal_queue[0][0]:
                            break
                    info[j][2] = info[j][2] - time_slice
                elif normal_queue[0][2] <= time_slice:
                    start_time.append(s_time)
                    s_time = s_time + normal_queue[0][2]
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(normal_queue[0][0])
                    for j in range(len(info)):
                        if info[j][0] == normal_queue[0][0]:
                            break
                    info[j][2] = 0
                    info[j][3] = 1
                    info[j].append(e_time)
        t_time = RoundRobin.calculateTurnaroundTime(self, info)
        w_time = RoundRobin.calculateWaitingTime(self, info)
        RoundRobin.printData(self, info, t_time, w_time, executed_process)

    def calculateTurnaroundTime(self, info):
        total_turnaround_time = 0
        for i in range(len(info)):
            turnaround_time = info[i][5] - info[i][1]
            total_turnaround_time = total_turnaround_time + turnaround_time
            info[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(info)
        return average_turnaround_time

    def calculateWaitingTime(self, info):
        total_waiting_time = 0
        for i in range(len(info)):
            waiting_time = info[i][6] - info[i][4]
            total_waiting_time = total_waiting_time + waiting_time
            info[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(info)
        return average_waiting_time

    def printData(self, info, average_turnaround_time, average_waiting_time, executed_process):
        info.sort(key=lambda x: x[0])
        print(f'Average Turnaround Time: {average_turnaround_time}')
        print(f'Average Waiting Time: {average_waiting_time}')
        print(f'Sequence of Processes: {executed_process}')


total_no_of_processes = int(input("Enter number of processes: "))
RoundRobin().collect_info(total_no_of_processes)
