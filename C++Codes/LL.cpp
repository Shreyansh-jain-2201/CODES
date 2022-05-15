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

Node *takeInput(int n)
{
    Node *head = NULL;
    Node *tail = NULL;
    for (int i = 0; i < n; i++)
    {
        int data;
        cin >> data;
        Node *n = new Node(data);
        if (head == NULL)
        {
            head = n;
            tail = n;
        }
        else
        {
            tail->next = n;
            tail = n;
        }
    }
    return head;
}
int length(Node *head)
{
    int count = 0;
    Node *temp = head;
    while (temp != NULL)
    {
        count = count + 1;
        temp = temp->next;
    }
    return count;
}
Node *insert(Node *head, int data, int i)
{
    int count = 0;
    Node *temp = head;
    Node *var;
    int len = length(head);
    if (i >= 0 && i <= len)
    {
        while (count < i - 1)
        {
            count = count + 1;
            temp = temp->next;
        }
        Node *n = new Node(data);
        var = temp->next;
        temp->next = n;
        n->next = var;
    }
    return head;
}

void print(Node *head)
{
    Node *temp = head;
    while (temp != NULL)
    {
        cout << temp->data << ' ';
        temp = temp->next;
    }
}

Node *deleteAtI(Node *&head, int i)

{
    if (i == 0)
        return head->next;
    int count = 1;
    Node *temp = head;
    int len = length(head);
    if (i >= 0 && i <= len)
    {
        while (count < i)
        {
            count = count + 1;
            temp = temp->next;
        }
        if (i == 0)
        {
            if (len > 1)
            {
                temp = head;
                temp->next = NULL;
                delete temp;
                head = head->next;
            }
            else
            {
                head = NULL;
            }
        }
        else if (i < len)
        {
            temp->next = temp->next->next;
        }
        else
        {
            temp->next = NULL;
        }
    }
    return head;
}

int main()
{
    int n;
    cin >> n;
    Node *head = takeInput(n);
    int data, i;
    cin >> i;
    head = deleteAtI(head, i);
    print(head);
    return 0;
}