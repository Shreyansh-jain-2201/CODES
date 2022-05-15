#include <stdlib.h>
#include <stdio.h>
#define NODES 7
#define MIN(X, Y) ((X) < (Y) ? (X) : (Y))
#define INFINITE 10000000

void push(const int *const *C, int **F, int *excess, int u, int v)
{
    int send = MIN(excess[u], C[u][v] - F[u][v]);
    F[u][v] += send;
    F[v][u] -= send;
    excess[u] -= send;
    excess[v] += send;
}

void relabel(const int *const *C, const int *const *F, int *h, int u)
{
    int v;
    int min_h = INFINITE;
    for (v = 0; v < NODES; v++)
    {
        if (C[u][v] - F[u][v] > 0)
        {
            min_h = MIN(min_h, h[v]);
            h[u] = min_h + 1;
        }
    }
};

void dis(const int *const *C, int **F, int *excess, int *h, int *seen, int u)
{
    while (excess[u] > 0)
    {
        if (seen[u] < NODES)
        {
            int v = seen[u];
            if ((C[u][v] - F[u][v] > 0) && (h[u] > h[v]))
            {
                push(C, F, excess, u, v);
            }
            else
            {
                seen[u] += 1;
            }
        }
        else
        {
            relabel(C, F, h, u);
            seen[u] = 0;
        }
    }
}

void move_to_front(int i, int *A)
{
    int temp = A[i];
    int n;
    for (n = i; n > 0; n--)
    {
        A[n] = A[n - 1];
    }
    A[0] = temp;
}

int push_relable(const int *const *C, int **F, int source, int sink)
{
    int *excess, *h, *list, *seen, i, p;

    excess = (int *)calloc(NODES, sizeof(int));
    h = (int *)calloc(NODES, sizeof(int));
    seen = (int *)calloc(NODES, sizeof(int));

    list = (int *)calloc((NODES - 2), sizeof(int));

    for (i = 0, p = 0; i < NODES; i++)
    {
        if ((i != source) && (i != sink))
        {
            list[p] = i;
            p++;
        }
    }

    h[source] = NODES;
    excess[source] = INFINITE;
    for (i = 0; i < NODES; i++)
        push(C, F, excess, source, i);

    p = 0;
    while (p < NODES - 2)
    {
        int u = list[p];
        int old_h = h[u];
        dis(C, F, excess, h, seen, u);
        if (h[u] > old_h)
        {
            move_to_front(p, list);
            p = 0;
        }
        else
        {
            p += 1;
        }
    }
    int maxflow = 0;
    for (i = 0; i < NODES; i++)
        maxflow += F[source][i];

    free(list);

    free(seen);
    free(h);
    free(excess);

    return maxflow;
}

int main()
{
    printf("\n\n\n\n\n");
    int **flow, **capacities, i;
    flow = (int **)calloc(NODES, sizeof(int *));
    capacities = (int **)calloc(NODES, sizeof(int *));
    for (i = 0; i < NODES; i++)
    {
        flow[i] = (int *)calloc(NODES, sizeof(int));
        capacities[i] = (int *)calloc(NODES, sizeof(int));
    }
    int n;
    printf("Enter the number of edges: ");
    scanf(" %d", &n);
    printf("Enter the number of source, destination and distances: \n");
    for (int i = 0; i < n; i++)
    {
        int s, t, d;
        scanf(" %d", &s);
        scanf(" %d", &t);
        scanf(" %d", &d);
        capacities[s][t] = d;
    }

    printf("Max Flow: %d", push_relable(capacities, flow, 0, 5));
    printf("\n\n\n\n\n");
    return 0;
}

// 7
// 0 1 13
// 0 2 10
// 1 3 7
// 1 5 6
// 2 1 3
// 3 4 5
// 4 5 10