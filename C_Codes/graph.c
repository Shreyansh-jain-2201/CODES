#include <stdio.h>
#include <stdlib.h>
#define N 6

struct Graph
{
    struct Node *head[N];
};

struct Node
{
    int destination;
    struct Node *next;
};

struct Edge
{
    int source, destination;
};

struct Graph *create_graph(struct Edge edges[], int n)
{
    struct Graph *graph = (struct Graph *)malloc(sizeof(struct Graph));

    for (int i = 0; i < N; i++)
    {
        graph->head[i] = NULL;
    }

    for (int i = 0; i < n; i++)
    {
        int source = edges[i].source;
        int destination = edges[i].destination;

        struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
        newNode->destination = destination;

        newNode->next = graph->head[source];

        graph->head[source] = newNode;
    }

    return graph;
}

void display(struct Graph *graph)
{
    for (int i = 0; i < N; i++)
    {
        struct Node *ptr = graph->head[i];
        if (ptr == NULL)
        {
            printf("NULL");
        }
        else
        {
            while (ptr != NULL)
            {
                printf("(%d --> %d)\t", i, ptr->destination);
                ptr = ptr->next;
            }
        }

        printf("\n");
    }
}

int main()
{
    int n;
    printf("Enter the number of edges: ");
    scanf("%d", &n);
    struct Edge edges[n];
    int distance[n];
    printf("Enter the source, destination and edge length of %d edges separated by a space: \n", n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &edges[i].source);
        scanf("%d", &edges[i].destination);
        scanf("%d", &distance[i]);
    }

    struct Graph *graph = create_graph(edges, n);

    printf("The required graph is \n");
    display(graph);

    return 0;
}