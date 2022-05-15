class sjf_premptive:
    
    def collect_info(self, n):
        info_list = []
        for i in range(n):
            temp = []
            process_id = int(input("Enter Process ID: "))
            arrival_time = int(input(f"Enter Arrival Time for Process {process_id}: "))
            burst_time = int(input(f"Enter Burst Time for Process {process_id}: "))
            temp.extend([process_id, arrival_time, burst_time, 0, burst_time])
            info_list.append(temp)
        sjf_premptive.gantt(self, info_list)

    def gantt(self, info_list):
        start_time = []
        completion_time = []
        s_time = 0
        sequence_of_process = []
        info_list.sort(key=lambda x: x[1])
        while 1:
            ready_queue = []
            normal_queue = []
            temp = []
            for i in range(len(info_list)):
                if info_list[i][1] <= s_time and info_list[i][3] == 0:
                    temp.extend([info_list[i][0], info_list[i][1], info_list[i][2], info_list[i][4]])
                    ready_queue.append(temp)
                    temp = []
                elif info_list[i][3] == 0:
                    temp.extend([info_list[i][0], info_list[i][1], info_list[i][2], info_list[i][4]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break
            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[2])
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                completion_time.append(e_time)
                sequence_of_process.append(ready_queue[0][0])
                for k in range(len(info_list)):
                    if info_list[k][0] == ready_queue[0][0]:
                        break
                info_list[k][2] = info_list[k][2] - 1
                if info_list[k][2] == 0:
                    info_list[k][3] = 1
                    info_list[k].append(e_time)
            if len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                completion_time.append(e_time)
                sequence_of_process.append(normal_queue[0][0])
                for k in range(len(info_list)):
                    if info_list[k][0] == normal_queue[0][0]:
                        break
                info_list[k][2] = info_list[k][2] - 1
                if info_list[k][2] == 0:
                    info_list[k][3] = 1
                    info_list[k].append(e_time)
        t_time = sjf_premptive.calculateTurnaroundTime(self, info_list)
        w_time = sjf_premptive.calculateWaitingTime(self, info_list)
        sjf_premptive.print_info(self, info_list, t_time, w_time, sequence_of_process)

    def calculateTurnaroundTime(self, info_list):
        total_turnaround_time = 0
        for i in range(len(info_list)):
            turnaround_time = info_list[i][5] - info_list[i][1]
            total_turnaround_time = total_turnaround_time + turnaround_time
            info_list[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(info_list)
        return average_turnaround_time

    def calculateWaitingTime(self, info_list):
        total_waiting_time = 0
        for i in range(len(info_list)):
            waiting_time = info_list[i][6] - info_list[i][4]
            total_waiting_time = total_waiting_time + waiting_time
            info_list[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(info_list)
        return average_waiting_time

    def print_info(self, info_list, average_turnaround_time, average_waiting_time, sequence_of_process):
        info_list.sort(key=lambda x: x[0])

        print(f'Average Turnaround Time: {average_turnaround_time}')
        print(f'Average Waiting Time: {average_waiting_time}')
        print(f'Sequence of Process: {sequence_of_process}')

n = int(input("Enter number of processes: "))
sjf = sjf_premptive()
sjf.collect_info(n)