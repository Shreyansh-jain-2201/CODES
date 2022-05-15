def firstFit(blockSize, noOfBlocks, processSize, noOfProcesses):
    allocation = [-1] * noOfProcesses
    for i in range(noOfProcesses):
        for j in range(noOfBlocks):
            if blockSize[j] >= processSize[i]:
                allocation[i] = j
                blockSize[j] -= processSize[i]
                break

    print("Process ID Process Size Block no.")
    for i in range(noOfProcesses):
        allocationStatus = ''
        if allocation[i] != -1:
            allocationStatus = allocation[i] + 1
        else:
            allocationStatus = "Not Allocated"
        print(
            f"   P{i+1}          {processSize[i]}       {allocationStatus}")


print("______Program for First Fit algorithm______\n")
noOfBlocks = int(input("Enter the number of blocks: "))
blockSize = []
for i in range(noOfBlocks):
    blockSize.append(int(input(f"Enter the block size for block B{i+1}: ")))

noOfProcesses = int(input("Enter the number of Processes: "))
processSize = []
for i in range(noOfProcesses):
    processSize.append(
        int(input(f"Enter the process size for process P{i+1}: ")))

firstFit(blockSize, noOfBlocks, processSize, noOfProcesses)
