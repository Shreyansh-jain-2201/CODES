#include <iostream>
#include <string>
#include <cstring>
#include <vector>

using namespace std;

void display(vector<int> x)
{
    int n = x.size();
    for (int i = 0; i < n; i++)
    {
        cout << x.at(i) << ' ';
    }
}

vector<int> add(vector<int> x, vector<int> y)
{
    vector<int> output;
    int n = x.size();
    for (int i = 0; i < n; i++)
    {
        output.push_back(x.at(i) + y.at(i));
    }
    return output;
}

vector<int> sub(vector<int> x, vector<int> y)
{
    vector<int> output;
    int n = x.size();
    for (int i = 0; i < n; i++)
    {
        output.push_back(x.at(i) - y.at(i));
    }
    return output;
}

bool isLessThan(vector<int> x, vector<int> y)
{
    int n = x.size();
    for (int i = 0; i < n; i++)
    {
        if (x.at(i) > y.at(i))
        {
            return false;
        }
    }
    return true;
}

bool isFinished(vector<bool> finish)
{
    int n = finish.size();
    for (int i = 0; i < n; i++)
    {
        if (!finish.at(i))
        {
            return false;
        }
    }
    return true;
}

void SafeSequence(vector<int> available, vector<vector<int>> allocation, vector<vector<int>> need, int noOfProcesses)
{
    vector<int> work;
    vector<bool> finish;
    vector<string> SafeSequence;
    int n = noOfProcesses;
    for (int i = 0; i < available.size(); i++)
        work.push_back(available[i]);

    for (int i = 0; i < n; i++)
    {
        finish.push_back(false);
    }
    for (int j = 0; j < n; j++)
    {
        for (int i = 0; i < n; i++)
        {
            if (isLessThan(need.at(i), work) && !finish.at(i))
            {
                work = add(work, allocation.at(i));
                finish.at(i) = true;
                SafeSequence.push_back("P" + to_string(i + 1));
                break;
            }
        }
        if (isFinished(finish))
        {
            break;
        }
    }
    if (isFinished(finish))
    {
        cout << "The Process is in Safe State." << endl;
        cout << "To prevent the deadlock, the processes must execute in the order: ";
        for (int i = 0; i < n; i++)
        {
            cout << SafeSequence.at(i) << " ";
        }
        cout << endl;
    }
    else
    {
        cout << "The system is in a deadlock state." << endl;
        cout << "The processes causing deadlock are: ";
        for (int i = 0; i < n; i++)
        {
            if (not finish.at(i))
            {
                cout << "P" << i + 1 << " ";
            }
        }
        cout << endl;
    }
}

int main()
{
    cout << endl
         << endl
         << endl
         << endl
         << endl;
    vector<int> available;
    vector<vector<int>> maximum;
    vector<vector<int>> allocation;
    vector<vector<int>> need;
    int noOfProcesses, noOfResources;
    cout << "Enter the total number of processes: ";
    cin >> noOfProcesses;
    cout << "Enter the total number of resources: ";
    cin >> noOfResources;
    cout << "Enter the available instances of of resources: ";
    for (int i = 0; i < noOfResources; i++)
    {
        int var;
        cin >> var;
        available.push_back(var);
    }
    vector<int> work = available;
    for (int i = 0; i < noOfProcesses; i++)
    {
        vector<int> pNeed;
        vector<int> pAllocation;
        cout << "Enter the need of resources of process P" << i + 1 << ": ";
        for (int j = 0; j < noOfResources; j++)
        {
            int var;
            cin >> var;
            pNeed.push_back(var);
        }
        cout << "Enter the allocated resources of process P" << i + 1 << ": ";
        for (int j = 0; j < noOfResources; j++)
        {
            int var;
            cin >> var;
            pAllocation.push_back(var);
        }
        need.push_back(pNeed);
        allocation.push_back(pAllocation);
        vector<int> var = add(pNeed, pAllocation);
        maximum.push_back(var);
    }
    SafeSequence(available, allocation, need, noOfProcesses);
    string moreRequest;
    cout << "Does any process want to make an immediate additional request claim?(Yes/No): ";
    cin >> moreRequest;
    int processId = -1;
    while (moreRequest == "Yes")
    {
        vector<int> request;
        cout << "Enter the process ID of the process making the claim: ";
        string var;
        cin >> var;
        int processId = stoi(var.substr(var.length() - 1, 1)) - 1;
        cout << "Enter the request of the process P" << processId + 1 << ": ";
        for (int i = 0; i < noOfResources; i++)
        {
            int var;
            cin >> var;
            request.push_back(var);
        }
        if (isLessThan(request, need.at(processId)))
        {
            if (isLessThan(request, available))
            {
                vector<vector<int>> allocationNew;
                vector<vector<int>> needNew;
                for (int i = 0; i < allocation.size(); i++)
                {
                    allocationNew.push_back(allocation[i]);
                    needNew.push_back(need[i]);
                }
                allocationNew[processId] = add(allocation[processId], request);
                needNew[processId] = sub(need[processId], request);

                SafeSequence(sub(available, request), allocationNew, needNew, noOfProcesses);
            }
            else
            {
                cout << "The available resources are less than the requested resources. The process must wait." << endl;
            }
        }
        else
        {
            cout << "The resources requested are more than the maximum allowed. Request terminated. " << endl;
        }
        cout << "Does any process want to make an immediate additional request claim?(Yes/No): ";
        cin >> moreRequest;
    }
    cout << endl
         << "Program finished execution." << endl
         << endl
         << endl
         << endl
         << endl
         << endl;

    return 0;
}

// 3
// 2
// 0 0
// 0 1
// 1 0
// 1 0
// 0 1
// 1 0
// 0 1

// 3
// 2
// 0 0
// 1 0
// 0 1
// 0 1
// 1 0
// 0 0
// 1 0
