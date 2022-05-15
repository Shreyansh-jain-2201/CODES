# print("\n\n\n\n")
# def add(matrix1, matrix2):
#     output = []
#     for i in range(len(matrix1)):
#         output.append(matrix1[i] + matrix2[i])
#     return output


# def sub(matrix1, matrix2):
#     output = []
#     for i in range(len(matrix1)):
#         output.append(matrix1[i] - matrix2[i])
#     return output


# def isLess(matrix1, matrix2):
#     for i in range(len(matrix1)):
#         if matrix1[i] > matrix2[i]:
#             return False
#     return True
        

# def isFinished(finish):
#     for i in range(len(finish)):
#         if not finish[i]:
#             return False
#     return True

# def generateSafeSequence(available, allocation, need, noOfProcesses):
#     work = available
#     finish = []
#     safeSequence = []
#     for i in range(noOfProcesses):
#         finish.append(False)
#     for j in range(noOfProcesses):
#         for i in range(noOfProcesses):
#             if isLess(need[i], work) and not finish[i]:
#                 work = add(work, allocation[i])
#                 finish[i] = True
#                 safeSequence.append(f"P{i+1}")
#                 break
#         if isFinished(finish):
#             break
#     if isFinished(finish):
#         sequence = ""
#         for i in range(noOfProcesses):
#             sequence += " " + safeSequence[i]
#         print(f"To prevent the deadlock, the process must be executed in the following Safe Sequence: {sequence}.")
#     else:
#         print(f"The system is in a deadlock state.")
        
# available = []
# maximum = []
# allocation = []
# need = []
# noOfProcesses = int(input("Enter the total number of processes: "))
# noOfResources = int(input("Enter the total number of resources: "))

# available = input(f"Enter the available instances of resources: ").split(" ")
# work = available
# for i in range(noOfResources):
#     available[i] = int(available[i])

# for i in range(noOfProcesses):
#     processMAX = input(f"Enter the maximum requirement of resources of process P{i + 1}: ").split(" ")
#     processAllocation = input(f"Enter the allocated resources of process P{i + 1}: ").split(" ")
#     for j in range(noOfResources):
#         processMAX[j] = int(processMAX[j])
#         processAllocation[j] = int(processAllocation[j])
#     maximum.append(processMAX)
#     allocation.append(processAllocation)
#     need.append(sub(processMAX, processAllocation))
    
# generateSafeSequence(available, allocation, need, noOfProcesses)

# additionalClaim = input("Does any process want to make an immediate additional request claim?(Yes/No): ").upper()
# processId = -1
# while additionalClaim == "YES":
#     processId = int(input("Enter the process ID of the process making the claim: ")[-1]) - 1
#     request = input(f"Enter the request of the process P{processId + 1}: ").split(" ")
#     for i in range(len(request)):
#         request[i] = int(request[i])
#     if isLess(request, need[processId]):
#         if isLess(request, available):
#             need_new = need
#             allocation_new = allocation
#             allocation_new[processId] = add(allocation[processId], request)
#             need_new[processId] = sub(need[processId], request)
#             generateSafeSequence(sub(available, request), allocation_new, need_new, noOfProcesses)
#         else:
#             print("The available resources are less than the requested resources. The process must wait.")
#     else:
#         print("The resources requested are more than the maximum allowed. Request terminated. ")
#     additionalClaim = input("Does any process want to make an immediate additional request claim?(Yes/No): ").upper()
    
    
# print("________________Program Terminated________________")
# print("\n\n\n\n")
 
# 5
# 3
# 3 3 2
# 7 5 3
# 0 1 0
# 3 2 2
# 2 0 0
# 9 0 2
# 3 0 2
# 2 2 2
# 2 1 1
# 4 3 3
# 0 0 2
# Yes
# P2
# 1 0 2
# No


# 5
# 3
# 3 3 2
# 7 5 3
# 0 1 0
# 3 2 2
# 2 0 0
# 9 0 2
# 3 0 2
# 2 2 9
# 2 1 1
# 4 3 3
# 0 0 2
# Yes
# P2
# 1 0 2
# No

# import threading
# import random
# import time

# #inheriting threading class in Thread module
# class Philosopher(threading.Thread):
#     running = True  #used to check if everyone is finished eating

#  #Since the subclass overrides the constructor, it must make sure to invoke the base class constructor (Thread.__init__()) before doing anything else to the thread.
#     def __init__(self, index, forkOnLeft, forkOnRight):
#         threading.Thread.__init__(self)
#         self.index = index
#         self.forkOnLeft = forkOnLeft
#         self.forkOnRight = forkOnRight

#     def run(self):
#         while(self.running):
#             # Philosopher is thinking (but really is sleeping).
#             time.sleep(30)
#             print ('Philosopher %s is hungry.' % self.index)
#             self.dine()

#     def dine(self):
#         # if both the semaphores(forks) are free, then philosopher will eat
#         fork1, fork2 = self.forkOnLeft, self.forkOnRight
#         while self.running:
#             fork1.acquire() # wait operation on left fork
#             locked = fork2.acquire(False) 
#             if locked: break #if right fork is not available leave left fork
#             fork1.release()
#             print ('Philosopher %s swaps forks.' % self.index)
#             fork1, fork2 = fork2, fork1
#         else:
#             return
#         self.dining()
#         #release both the fork after dining
#         fork2.release()
#         fork1.release()
 
#     def dining(self):			
#         print ('Philosopher %s starts eating. '% self.index)
#         time.sleep(30)
#         print ('Philosopher %s finishes eating and leaves to think.' % self.index)

# def main():
#     forks = [threading.Semaphore() for n in range(5)] #initialising array of semaphore i.e forks

#     #here (i+1)%5 is used to get right and left forks circularly between 1-5
#     philosophers= [Philosopher(i, forks[i%5], forks[(i+1)%5])
#             for i in range(5)]

#     Philosopher.running = True
#     for p in philosophers: p.start()
#     time.sleep(100)
#     Philosopher.running = False
#     print ("Now we're finishing.")
 

# if __name__ == "__main__":
#     main()

import multiprocessing
import time
import datetime
import random
import pickle
import abc

from network import SocketServer
from network import SocketClient
from network import DatagramServerSocket
from network import DatagramSocketClient
from fork_address import get_fork
from fork_address import get_fork_left
from fork_address import get_fork_right
from fork_address import get_number_of_forks


class Child(object):
    @abc.abstractmethod
    def stop(self):
        pass


class Fork(SocketServer, Child):
    def __init__(self, identifier, host, port):
        self.id = identifier
        self.being_used = False
        self.being_used_by = None
        super(Fork, self).__init__(host, port)

    def start(self):
        self.run = True
        super(Fork, self).start()

    def stop(self):
        self.run = False
        super(Fork, self).stop()

    def handle_connection(self, connection):
        while self.run:
            try:
                data = connection.recv(1024)
                if data:
                    request = pickle.loads(data)  # request -> [philosopher_id, action]
                    # If the request action is acquiring the fork
                    if request[1] == 1:
                        if self.being_used:  # If fork is dirty/being used
                            # Send [fork_id, philosopher_id, action, success]
                            # action  = 1 for acquiring fork
                            # success = 0 for failure
                            connection.send(pickle.dumps([self.id, request[0], 1, 0]))
                            break
                        else:  # If fork is clean/not being used
                            self.being_used = True
                            self.being_used_by = request[0]  # Store the id of the philosopher who has the fork now
                            # Send [fork_id, philosopher_id, action, success]
                            # action  = 1 for acquiring fork
                            # success = 1 for success
                            connection.send(pickle.dumps([self.id, self.being_used_by, 1, 1]))
                    # If the request action is releasing the fork
                    elif request[1] == 0:
                        # Fork has to be dirty/being used
                        # Release request can only be made by the philosopher holding the fork
                        if self.being_used and self.being_used_by == request[0]:
                            last_user = self.being_used_by
                            self.being_used = False
                            self.being_used_by = None
                            # Send [fork_id, philosopher_id, action, success]
                            # action  = 0 for releasing fork
                            # success = 1 for success
                            connection.send(pickle.dumps([self.id, last_user, 0, 1]))
                            break
                        else:
                            # Send [fork_id, philosopher_id, action, success]
                            # action  = 0 for releasing fork
                            # success = 0 for failure
                            connection.send(pickle.dumps([self.id, request[0], 0, 0]))
                            break
            except:
                break
        connection.close()


class Philosopher(Child):
    def __init__(self, identifier, fork_left, fork_right):
        self.id = identifier
        self.fork_left = fork_left
        self.fork_right = fork_right
        self.run = False

    def start(self):
        self.run = True
        while self.run:
            self.report_status(pickle.dumps([self.id, 0]))  # IS THINKING
            time.sleep(random.randint(1, 3))
            self.dine()

    def stop(self):
        self.run = False

    def dine(self):
        fork_l, fork_r = self.fork_left, self.fork_right
        self.report_status(pickle.dumps([self.id, 1]))  # IS WAITING
        client = None
        client2 = None
        while self.run:
            client = self.acquire_blocking(fork_l)  # MUST get the left fork
            is_available = self.acquire_non_blocking(fork_r)  # TRY to get the right fork
            # is_available = [acquired, client]
            # acquired -> True/False
            client2 = is_available[1]
            if not is_available[0]:  # If left fork not acquired
                self.release_fork(client)  # Release the left fork
                fork_l, fork_r = fork_r, fork_l  # Swap the forks, so that next time you acquire the right fork first
            else:
                break

        if self.run:
            self.dining()
            # Release both forks after done eating
            self.release_fork(client)
            self.release_fork(client2)
        else:
            if client:
                client.close()
            if client2:
                client2.close()

    def dining(self):
        self.report_status(pickle.dumps([self.id, 2]))  # IS EATING
        time.sleep(random.randint(3, 6))

    def release_fork(self, client):
        client.send(pickle.dumps([self.id, 0]))  # Sends [id, 0] to server. 0 being command for releasing the fork
        data = client.receive()
        if data:
            response = pickle.loads(data)
            # response -> [fork_id, philosopher_id, action, success]
            # action   -> 1 = acquiring the fork, 0 = releasing the fork
            # success  -> 1 = successful, 0 = failure
            if response[1] == self.id and response[2] == 0 and response[3] == 1:
                client.close()
            else:
                pass

    # Blocks the execution until the client acquires the fork
    def acquire_blocking(self, fork):
        while self.run:
            try:
                time.sleep(0.2)
                client = SocketClient()
                client.connect(fork[0], fork[1])
                client.send(pickle.dumps([self.id, 1]))
                data = client.receive()
                if data:
                    response = pickle.loads(data)
                    # response -> [fork_id, philosopher_id, action, success]
                    # action   -> 1 = acquiring the fork, 0 = releasing the fork
                    # success  -> 1 = successful, 0 = failure
                    if response[1] == self.id and response[2] == 1 and response[3] == 1:
                        return client
                client.close()
            except:
                pass

    # Doesn't block the execution if client cannot acquire the fork
    def acquire_non_blocking(self, fork):
        client = SocketClient()
        client.connect(fork[0], fork[1])
        client.send(pickle.dumps([self.id, 1]))
        data = client.receive()
        if data:
            response = pickle.loads(data)
            # response -> [fork_id, philosopher_id, action, success]
            # action   -> 1 = acquiring the fork, 0 = releasing the fork
            # success  -> 1 = successful, 0 = failure
            if response[1] == self.id and response[2] == 1 and response[3] == 1:
                return [True, client]
        client.close()
        return [False, client]

    @staticmethod
    def report_status(msg):
        client = DatagramSocketClient()
        client.send('localhost', 6000, msg)
        client.close()


class StatusDisplayModule(DatagramServerSocket, Child):
    def __init__(self, number_of_philosophers):
        self.num = number_of_philosophers
        self.headers = ['Current Time']
        self.divider_line = '----------------------'
        self.display_format = '{: >20} '
        for i in range(number_of_philosophers):
            self.headers.append("Philosopher " + str(i))
            if i != (number_of_philosophers - 1):
                self.display_format += "{: >20} "
            else:
                self.display_format += "{: >20}"
            self.divider_line += "----------------------"
        print("\n\nDining Philosophers Problem: By Sagun Pandey and Shelby LeBlanc\n\n")
        print(self.display_format.format(*self.headers))
        print(self.divider_line)
        super(StatusDisplayModule, self).__init__("localhost", 6000)

    def start(self):
        super(StatusDisplayModule, self).start()

    def stop(self):
        super(StatusDisplayModule, self).stop()
        super(StatusDisplayModule, self).close()

    def handle_data(self, data):
        state = []

        response = pickle.loads(data[0])
        process_id = response[0]
        status_type = response[1]

        status = ""
        if status_type == 0:
            status = "Thinking"
        elif status_type == 1:
            status = "Waiting"
        elif status_type == 2:
            status = "Eating"

        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        state.append(current_time)

        for i in range(self.num):
            if i == process_id:
                state.append(status)
            else:
                state.append("********")

        print(self.display_format.format(*state))


def fork_process(identifier, address, port):
    fork = Fork(identifier, address, port)
    fork.start()


def philosopher_process(identifier, fork_left, fork_right):
    philosopher = Philosopher(identifier, fork_left, fork_right)
    philosopher.start()


def display_process(number_of_philosophers):
    display_module = StatusDisplayModule(number_of_philosophers)
    display_module.start()


display = None
fork_processes = []
philosophers_processes = []


def dining_philosophers():
    global fork_processes
    global philosophers_processes
    global display

    num_of_philosophers = get_number_of_forks()  # Number of Forks = Number of Philosophers

    # Create a Display Process
    display = multiprocessing.Process(target=display_process, args=(num_of_philosophers,))
    display.start()

    # Create Forks (Server Processes)
    for i in range(num_of_philosophers):
        fork_address = get_fork(i)
        fork = multiprocessing.Process(target=fork_process, args=(i, fork_address[0], fork_address[1],))
        fork_processes.append(fork)
        fork.start()

    # Create Philosophers (Client Processes)
    for i in range(num_of_philosophers):
        philosopher = multiprocessing.Process(target=philosopher_process,
                                              args=(i, get_fork_left(i), get_fork_right(i),))
        philosophers_processes.append(philosopher)
        philosopher.start()

    time.sleep(90)
    terminate()  # Terminate all child processes

    # Wait for all child processes to end
    while multiprocessing.active_children():
        time.sleep(1)


def terminate():
    global fork_processes
    global philosophers_processes
    global display

    display.terminate()
    for p in philosophers_processes:
        p.terminate()
    for f in fork_processes:
        f.terminate()


if __name__ == "__main__":
    try:
        dining_philosophers()
    except KeyboardInterrupt:
        terminate()