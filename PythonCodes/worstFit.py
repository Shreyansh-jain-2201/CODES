def worstFit(blockSize, noOfBlocks, processSize, noOfProcesses):
    allocation = [-1] * noOfProcesses
    for i in range(noOfProcesses):
        worst = -1
        for j in range(noOfBlocks):
            if blockSize[j] >= processSize[i]:
                if worst == -1:
                    worst = j
                elif blockSize[worst] < blockSize[j]:
                    worst = j
        if worst != -1:
            allocation[i] = worst
            blockSize[worst] -= processSize[i]
    print("Process ID Process Size Block no.")
    for i in range(noOfProcesses):
        allocationStatus = ''
        if allocation[i] != -1:
            allocationStatus = allocation[i] + 1
        else:
            allocationStatus = "Not Allocated"
        print(
            f"   P{i+1}          {processSize[i]}       {allocationStatus}")


print("______Program for Worst Fit Algorithm______\n")
noOfBlocks = int(input("Enter the number of blocks: "))
blockSize = []
for i in range(noOfBlocks):
    blockSize.append(int(input(f"Enter the block size for block B{i+1}: ")))

noOfProcesses = int(input("Enter the number of Processes: "))
processSize = []
for i in range(noOfProcesses):
    processSize.append(
        int(input(f"Enter the process size for process P{i+1}: ")))

worstFit(blockSize, noOfBlocks, processSize, noOfProcesses)
