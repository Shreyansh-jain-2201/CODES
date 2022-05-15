#include <iostream>

using namespace std;

class Node
{
    public:
        int data;
        Node *next;
    Node(int data)
    {
        this->data = data;
        this->next = NULL;
    }
};

Node* takeInput()
{
    Node *head = NULL;
    Node *tail = NULL;
    int data;
    cin >> data;
    while(data != -1)
    {
        Node *n = new Node(data);
        if(head == NULL)
        {
            head = n;
            tail = n;
        }
        else
        {
            tail -> next = n;
            tail = n;
            // n -> next = head;
            // head = n;
        }
        cin >> data;
    }
    return head;
}

void print(Node *head)
{
    Node *temp = head;
    while(temp != NULL)
    {
        cout << temp->data<<" ";
        temp = temp ->next;
    }
    cout<<endl;
}
int length(Node *head)
{
    int count = 0;
    Node *temp = head;
    while(temp != NULL)
    {
        count = count + 1;
        temp = temp ->next;
    }
    return count;
}
int printIthNode(Node *head, int i)
{
    int count = 0;
    Node *temp = head;
    while(count < i)
    {
        count = count + 1;
        temp = temp ->next;
    }
    return temp->data;
}

void insertAtI(Node *head, int data, int i)
{
    int count = 0;
    Node *temp = head;
    Node *var;
    int len = length(head);
    if (i >= 0 && i <= len)
    {
        while(count < i-1)
        {
            count = count + 1;
            temp = temp ->next;
        }
        Node *n = new Node(data);
        var = temp -> next;
        temp->next = n;
        n->next = var;
    }
}

void deleteAtI(Node *&head, int i)

{
    int count = 1;
    Node *temp = head;
    int len = length(head);
    if (i >= 0 && i <= len)
    {
        while(count < i)
        {
            count = count + 1;
            temp = temp ->next;
        }
        if(i == 0)
        {
            if(len > 1)
            {
                temp = head;
                temp-> next = NULL;
                delete temp;
                head = head -> next;
            }
            else
            {
                head = NULL;
            }
        }
        else if(i < len)
        {
            temp->next= temp->next->next;
        }
        else
        {
            temp->next = NULL;
        }
    }
}

int main()

{
    Node *head = takeInput();
    print(head);
    cout<<endl<<length(head)<<endl<<printIthNode(head, 3)<<endl;
    insertAtI(head, 99, 7);
    print(head);
    int i;
    cin >> i;
    deleteAtI(head, 0);
    print(head);

return 0;
}