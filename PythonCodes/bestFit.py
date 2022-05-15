def bestFit(blockSize, noOfBlocks, processSize, noOfProcesses):
    allocation = [-1] * noOfProcesses
    for i in range(noOfProcesses):
        best = -1
        for j in range(noOfBlocks):
            if blockSize[j] >= processSize[i]:
                if best == -1:
                    best = j
                elif blockSize[best] > blockSize[j]:
                    best = j
        if best != -1:
            allocation[i] = best
            blockSize[best] -= processSize[i]
    print("Process ID Process Size Block no.")
    for i in range(noOfProcesses):
        allocationStatus = ''
        if allocation[i] != -1:
            allocationStatus = allocation[i] + 1
        else:
            allocationStatus = "Not Allocated"
        print(
            f"   P{i+1}          {processSize[i]}       {allocationStatus}")


print("______Program for Best Fit Algorithm______\n")
noOfBlocks = int(input("Enter the number of blocks: "))
blockSize = []
for i in range(noOfBlocks):
    blockSize.append(int(input(f"Enter the block size for block B{i+1}: ")))

noOfProcesses = int(input("Enter the number of Processes: "))
processSize = []
for i in range(noOfProcesses):
    processSize.append(
        int(input(f"Enter the process size for process P{i+1}: ")))

bestFit(blockSize, noOfBlocks, processSize, noOfProcesses)


# 5
# 100
# 500
# 200
# 300
# 600
# 4
# 212
# 417
# 112
# 426
