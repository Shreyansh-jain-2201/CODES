// #include <bits/stdc++.h>
// using namespace std;

// struct Edge
// {
//     // To store current flow and capacity of edge
//     int flow, capacity;

//     // An edge u--->v has start vertex as u and end
//     // vertex as v.
//     int u, v;

//     Edge(int flow, int capacity, int u, int v)
//     {
//         this->flow = flow;
//         this->capacity = capacity;
//         this->u = u;
//         this->v = v;
//     }
// };

// // Represent a Vertex
// struct Vertex
// {
//     int h, e_flow;

//     Vertex(int h, int e_flow)
//     {
//         this->h = h;
//         this->e_flow = e_flow;
//     }
// };

// // To represent a flow network
// class Graph
// {
//     int V; // No. of vertices
//     vector<Vertex> ver;
//     vector<Edge> edge;

//     // Function to push excess flow from u
//     bool push(int u);

//     // Function to relabel a vertex u
//     void relabel(int u);

//     // This function is called to initialize
//     // preflow
//     void preflow(int s);

//     // Function to reverse edge
//     void updateReverseEdgeFlow(int i, int flow);

// public:
//     Graph(int V); // Constructor

//     // function to add an edge to graph
//     void addEdge(int u, int v, int w);

//     // returns maximum flow from s to t
//     int getMaxFlow(int s, int t);
// };

// Graph::Graph(int V)
// {
//     this->V = V;

//     // all vertices are initialized with 0 height
//     // and 0 excess flow
//     for (int i = 0; i < V; i++)
//         ver.push_back(Vertex(0, 0));
// }

// void Graph::addEdge(int u, int v, int capacity)
// {
//     // flow is initialized with 0 for all edge
//     edge.push_back(Edge(0, capacity, u, v));
// }

// void Graph::preflow(int s)
// {
//     // Making h of source Vertex equal to no. of vertices
//     // Height of other vertices is 0.
//     ver[s].h = ver.size();

//     //
//     for (int i = 0; i < edge.size(); i++)
//     {
//         // If current edge goes from source
//         if (edge[i].u == s)
//         {
//             // Flow is equal to capacity
//             edge[i].flow = edge[i].capacity;

//             // Initialize excess flow for adjacent v
//             ver[edge[i].v].e_flow += edge[i].flow;

//             // Add an edge from v to s in residual graph with
//             // capacity equal to 0
//             edge.push_back(Edge(-edge[i].flow, 0, edge[i].v, s));
//         }
//     }
// }

// // returns index of overflowing Vertex
// int overFlowVertex(vector<Vertex> &ver)
// {
//     for (int i = 1; i < ver.size() - 1; i++)
//         if (ver[i].e_flow > 0)
//             return i;

//     // -1 if no overflowing Vertex
//     return -1;
// }

// // Update reverse flow for flow added on ith Edge
// void Graph::updateReverseEdgeFlow(int i, int flow)
// {
//     int u = edge[i].v, v = edge[i].u;

//     for (int j = 0; j < edge.size(); j++)
//     {
//         if (edge[j].v == v && edge[j].u == u)
//         {
//             edge[j].flow -= flow;
//             return;
//         }
//     }

//     // adding reverse Edge in residual graph
//     Edge e = Edge(0, flow, u, v);
//     edge.push_back(e);
// }

// // To push flow from overflowing vertex u
// bool Graph::push(int u)
// {
//     // Traverse through all edges to find an adjacent (of u)
//     // to which flow can be pushed
//     for (int i = 0; i < edge.size(); i++)
//     {
//         // Checks u of current edge is same as given
//         // overflowing vertex
//         if (edge[i].u == u)
//         {
//             // if flow is equal to capacity then no push
//             // is possible
//             if (edge[i].flow == edge[i].capacity)
//                 continue;

//             // Push is only possible if height of adjacent
//             // is smaller than height of overflowing vertex
//             if (ver[u].h > ver[edge[i].v].h)
//             {
//                 // Flow to be pushed is equal to minimum of
//                 // remaining flow on edge and excess flow.
//                 int flow = min(edge[i].capacity - edge[i].flow,
//                                ver[u].e_flow);

//                 // Reduce excess flow for overflowing vertex
//                 ver[u].e_flow -= flow;

//                 // Increase excess flow for adjacent
//                 ver[edge[i].v].e_flow += flow;

//                 // Add residual flow (With capacity 0 and negative
//                 // flow)
//                 edge[i].flow += flow;

//                 updateReverseEdgeFlow(i, flow);

//                 return true;
//             }
//         }
//     }
//     return false;
// }

// // function to relabel vertex u
// void Graph::relabel(int u)
// {
//     // Initialize minimum height of an adjacent
//     int mh = INT_MAX;

//     // Find the adjacent with minimum height
//     for (int i = 0; i < edge.size(); i++)
//     {
//         if (edge[i].u == u)
//         {
//             // if flow is equal to capacity then no
//             // relabeling
//             if (edge[i].flow == edge[i].capacity)
//                 continue;

//             // Update minimum height
//             if (ver[edge[i].v].h < mh)
//             {
//                 mh = ver[edge[i].v].h;

//                 // updating height of u
//                 ver[u].h = mh + 1;
//             }
//         }
//     }
// }

// // main function for printing maximum flow of graph
// int Graph::getMaxFlow(int s, int t)
// {
//     preflow(s);

//     // loop untill none of the Vertex is in overflow
//     while (overFlowVertex(ver) != -1)
//     {
//         int u = overFlowVertex(ver);
//         if (!push(u))
//             relabel(u);
//     }

//     // ver.back() returns last Vertex, whose
//     // e_flow will be final maximum flow
//     return ver.back().e_flow;
// }

// // Driver program to test above functions
// int main()
// {
//     int V = 5;

//     Graph g(V);

//     g.addEdge(0, 1, 13);
//     g.addEdge(0, 2, 10);
//     g.addEdge(1, 3, 7);
//     g.addEdge(1, 5, 6);
//     g.addEdge(2, 1, 3);
//     g.addEdge(3, 4, 5);
//     g.addEdge(4, 5, 10);

//     int s = 0, t = 5;

//     cout << "Maximum flow is " << g.getMaxFlow(s, t);
//     return 0;
// }

#define DEBUG // comment when you have to disable all debug macros.
#define LOCAL
#define NDEBUG // comment when all assert statements have to be disabled.
#include <iostream>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <climits>
#include <ctime>
#include <algorithm>
#include <functional>
#include <stack>
#include <queue>
#include <list>
#include <deque>
#include <sys/time.h>
#include <iomanip>
#include <cstdarg>
#include <utility> //std::pair
#include <cassert>
#define tr(c, i) for (typeof(c.begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c, x) ((c).find(x) != (c).end())
#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair
#define log2(x) (log(x) / log(2))
#define ARRAY_SIZE(arr) (1 [&arr] - arr)
#define INDEX(arr, elem) (lower_bound(all(arr), elem) - arr.begin())
#define lld long long int
#define MOD 1000000007
#define gcd __gcd
#define equals(a, b) (a.compare(b) == 0) // for strings only
using namespace std;

struct Graph
{
    lld numV;
    vector<lld> *adj;
    lld **flow, **cap, **cf, *height, *excess;
    inline void SET0(lld *array)
    {
        for (lld i = 0; i <= numV; i++)
            array[i] = 0;
    }
    Graph(lld _numV)
    {
        numV = _numV;
        lld i;
        /* allocating memory....*/
        flow = new lld *[numV + 1];
        for (i = 0; i <= numV; i++)
            flow[i] = new lld[numV + 1], SET0(flow[i]);
        cap = new lld *[numV + 1];
        for (i = 0; i <= numV; i++)
            cap[i] = new lld[numV + 1], SET0(cap[i]);
        cf = new lld *[numV + 1];
        for (i = 0; i <= numV; i++)
            cf[i] = new lld[numV + 1], SET0(cf[i]);

        height = new lld[numV + 1];
        excess = new lld[numV + 1];
        SET0(height);
        SET0(excess);
        adj = new vector<lld>[numV + 1];
    }
    void addEdge(lld u, lld v, lld uv)
    {
        adj[u].push_back(v);
        cap[u][v] = uv;
        cf[u][v] = uv;
    }

    void initialize_preflow(lld source)
    {
        lld i, v;
        height[source] = numV - 1;

        tr(adj[source], it)
        {
            v = *it;
            flow[source][v] = cap[source][v];
            flow[v][source] = -cap[source][v];
            excess[v] += cap[source][v];
            excess[source] -= cap[source][v];
            cf[source][v] = cap[source][v] - flow[source][v];
            cf[v][source] = cap[v][source] - flow[v][source];
        }
    }
    void push(lld u, lld v)
    {
        lld push_val = min(cf[u][v], excess[u]);
        flow[u][v] += push_val;
        flow[v][u] = -flow[u][v];
        excess[u] -= push_val;
        excess[v] += push_val;
        cf[u][v] = cap[u][v] - flow[u][v];
        cf[v][u] = cap[v][u] - flow[v][u];
    }
    lld max_flow(lld source, lld sink)
    {
        initialize_preflow(source);
        queue<lld> q;
        bool considered[numV + 1];
        lld u, v, m, i;
        memset(considered, false, sizeof(considered));
        tr(adj[source], it)
        {
            v = *it;
            if (v != sink)
            {
                q.push(v);
                considered[v] = true;
            }
        }
        bool flag;
        u = -1;
        while (!q.empty())
        {

            u = q.front();
            m = -1;
            for (i = 0; i < adj[u].size() && excess[u] > 0; i++)
            {

                v = adj[u][i];
                if (cf[u][v] > 0)
                {
                    if (height[u] > height[v])
                    {
                        push(u, v);
                        if (!considered[v] && v != sink && v != source)
                        {
                            considered[v] = true;
                            q.push(v);
                        }
                    }
                    else if (m == -1)
                        m = height[v];
                    else
                        m = min(m, height[v]);
                }
            }

            if (adj[u].empty())
            {
                q.pop();
                continue;
            }
            if (excess[u] != 0)
                height[u] = m + 1;
            else
            {
                q.pop();
                considered[u] = false;
            }
        }
        return excess[sink];
    }
};

template <class T>
inline void inputInt(T &n)
{
    n = 0;
    T ch = getchar_unlocked();
    while (ch < '0' || ch > '9')
        ch = getchar_unlocked();
    while (ch >= '0' && ch <= '9')
        n = (n << 3) + (n << 1) + ch - '0', ch = getchar_unlocked();
}

int main()
{
#ifdef LOCAL
    freopen("input.in", "r", stdin);
#endif
    lld e, u, v, n, c;
    // cout<<"V:"<<endl;
    cin >> n >> e;

    Graph g(n);
    while (e--)
    {

        inputInt(u);
        inputInt(v);
        inputInt(c);
        if (u != v)
        {
            if (g.cf[u][v])
                g.cf[u][v] = g.cf[v][u] = g.cap[u][v] = g.cap[v][u] + c;
            else
                g.addEdge(u, v, c);
        }
    }
    cout << g.max_flow(1, n) << endl;
}