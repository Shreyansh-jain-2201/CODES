# print("\n\n\n\n")
def add(matrix1, matrix2):
    output = []
    for i in range(len(matrix1)):
        output.append(matrix1[i] + matrix2[i])
    return output


def sub(matrix1, matrix2):
    output = []
    for i in range(len(matrix1)):
        output.append(matrix1[i] - matrix2[i])
    return output


def isLess(matrix1, matrix2):
    for i in range(len(matrix1)):
        if matrix1[i] > matrix2[i]:
            return False
    return True


def isFinished(finish):
    for i in range(len(finish)):
        if not finish[i]:
            return False
    return True


def generateSafeSequence(available, allocation, need, noOfProcesses):
    work = available
    finish = []
    safeSequence = []
    for i in range(noOfProcesses):
        finish.append(False)
    for j in range(noOfProcesses):
        for i in range(noOfProcesses):
            if isLess(need[i], work) and not finish[i]:
                work = add(work, allocation[i])
                finish[i] = True
                safeSequence.append(f"P{i+1}")
                break
        if isFinished(finish):
            break
    if isFinished(finish):
        print(f"The process is in Safe State.")
        sequence = ""
        for i in range(noOfProcesses):
            sequence += " " + safeSequence[i]
        print(
            f"To prevent the deadlock, the process must be executed in the following Safe Sequence: {sequence}.")
    else:
        sequence = ""
        print(f"The system is in a deadlock state.")
        for i in range(len(finish)):
            if not finish[i]:
                sequence += f"P{i+1} "
        print(f"The processes causing deadlock is {sequence}")


available = []
maximum = []
allocation = []
need = []
noOfProcesses = int(input("Enter the total number of processes: "))
noOfResources = int(input("Enter the total number of resources: "))

available = input(f"Enter the available instances of resources: ").split(" ")
work = available
for i in range(noOfResources):
    available[i] = int(available[i])

for i in range(noOfProcesses):
    processNeed = input(
        f"Enter the need of resources of process P{i + 1}: ").split(" ")
    processAllocation = input(
        f"Enter the allocated resources of process P{i + 1}: ").split(" ")
    for j in range(noOfResources):
        processNeed[j] = int(processNeed[j])
        processAllocation[j] = int(processAllocation[j])
    need.append(processNeed)
    allocation.append(processAllocation)
    maximum.append(add(processNeed, processAllocation))

generateSafeSequence(available, allocation, need, noOfProcesses)

additionalClaim = input(
    "Does any process want to make an immediate additional request claim?(Yes/No): ").upper()
processId = -1
while additionalClaim == "YES":
    processId = int(
        input("Enter the process ID of the process making the claim: ")[-1]) - 1
    request = input(
        f"Enter the request of the process P{processId + 1}: ").split(" ")
    for i in range(len(request)):
        request[i] = int(request[i])
    if isLess(request, need[processId]):
        if isLess(request, available):
            need_new = need
            allocation_new = allocation
            allocation_new[processId] = add(allocation[processId], request)
            need_new[processId] = sub(need[processId], request)
            generateSafeSequence(sub(available, request),
                                 allocation_new, need_new, noOfProcesses)
        else:
            print(
                "The available resources are less than the requested resources. The process must wait.")
    else:
        print("The resources requested are more than the maximum allowed. Request terminated. ")
    additionalClaim = input(
        "Does any process want to make an immediate additional request claim?(Yes/No): ").upper()


print("________________Program Terminated________________")
# print("\n\n\n\n")


# 4
# 5
# 2 1 1 2 1
# 0 1 0 0 1
# 1 0 1 1 0
# 0 0 1 0 1
# 1 1 0 0 0
# 0 0 0 0 1
# 0 0 0 1 0
# 1 0 1 0 1
# 0 0 0 0 0
