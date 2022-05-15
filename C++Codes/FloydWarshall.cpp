
// #include <iostream>
// #include <vector>
// using namespace std;

// void printMatrix(vector<vector<int>> &m)
// {
//     int vertices = m.size();
//     for (int i = 0; i < vertices; i++)
//         cout << "\t" << i;
//     cout << "\n";
//     for (int i = 0; i < vertices; i++)
//     {
//         cout << i << "\t";
//         for (int j = 0; j < vertices; j++)
//             cout << m[i][j] << "\t";
//         cout << endl;
//     }
//     cout << endl;
// }

// void printPath(vector<vector<int>> &m, int i, int j)
// {
//     if (i == j)
//     {
//         cout << i;
//     }
//     else if (m[i][j] == -1)
//     {
//         cout << "Path does not exist";
//     }
//     else
//     {
//         printPath(m, i, m[i][j]);
//         cout << j;
//     }
// }

// int main()
// {

//     // Initialize
//     int vertices;
//     cout << "Enter the number of vertices: ";
//     cin >> vertices;
//     vector<vector<int>> d(vertices, vector<int>(vertices, 99));
//     vector<vector<int>> p(vertices, vector<int>(vertices, -1));

//     // Initialize diagonal
//     for (int i = 0; i < vertices; i++)
//         d[i][i] = 0;

//     for (int i = 0; i < vertices; i++)
//     {
//         for (int j = 0; j < vertices; j++)
//         {
//             if (i != j)
//             {
//                 int dist;
//                 cout << "Enter the distances between vertices " << i + 1 << " and " << j + 1 << ": ";
//                 cin >> dist;
//                 if (dist == -1)
//                 {
//                     d[i][j] = 99999999;
//                 }
//                 else
//                 {
//                     d[i][j] = dist;
//                 }
//             }
//         }
//     }
//     // Initialize distances
//     // 3
//     // 8
//     // 4
//     // 1
//     // 7
//     // 4
//     // 2
//     // 5
//     // 6
//     // d[0][1] = 3;
//     // d[0][2] = 8;
//     // d[0][4] = 4;
//     // d[1][3] = 1;
//     // d[1][4] = 7;
//     // d[2][1] = 4;
//     // d[3][0] = 2;
//     // d[3][2] = 5;
//     // d[4][3] = 6;

//     // Initialize predecessor
//     for (int i = 0; i < vertices; i++)
//         for (int j = 0; j < vertices; j++)
//             if (i != j && d[i][j] != 99)
//             {
//                 p[i][j] = i;
//             }

//     // Print out neighbour matrix
//     cout << "Distance matrix" << endl;
//     printMatrix(d);

//     // Print out path matrix
//     cout << "Path matrix" << endl;
//     printMatrix(p);

//     // Floyd-Warshall
//     for (int k = 0; k < vertices; k++)
//         for (int i = 0; i < vertices; i++)
//             for (int j = 0; j < vertices; j++)
//                 if (d[i][j] > d[i][k] + d[k][j])
//                 {
//                     d[i][j] = d[i][k] + d[k][j];
//                     p[i][j] = p[k][j];
//                 }

//     // Print out final distance matrix
//     cout << "Distance matrix" << endl;
//     printMatrix(d);

//     // Print out final path matrix
//     printMatrix(p);

//     return 0;
// }
#include <iostream>
using namespace std;
#include <climits>
#include <stack>

int mat[10][10];
int matNext[10][10];

void inicializaMatriz()
{
    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            mat[i][j] = INT_MAX / 4;
            matNext[i][j] = 0;
        }
    }
    for (int i = 0; i < 10; i++)
    {
        mat[i][i] = 0;
        matNext[i][i] = i + 1;
    }
}

void printMat(int n)
{
    cout << endl;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << mat[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
}

void printMatNext(int n)
{
    cout << endl;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << matNext[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
}

void floyd(int n)
{
    for (int k = 0; k < n; k++)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (mat[i][k] + mat[k][j] < mat[i][j])
                {
                    matNext[i][j] = k + 1;
                    mat[i][j] = mat[i][k] + mat[k][j];
                    // printMatNext(n);
                }
            }
        }
    }
}

void displayRoute(int n1, int n2)
{
    stack<int> s;
    while (matNext[n1][n2] != 0)
    {
        s.push(matNext[n1][n2]);
        n2 = matNext[n1][n2] - 1;
    }
    while (!s.empty())
    {
        cout << "-" << s.top();
        s.pop();
    }
}

int main()
{
    inicializaMatriz();

    int nodes, arcs;
    cin >> nodes >> arcs;
    for (int i = 0; i < arcs; i++)
    {
        int n1, n2, val;
        cin >> n1 >> n2 >> val;
        mat[n1 - 1][n2 - 1] = val;
        mat[n2 - 1][n1 - 1] = val;
    }

    floyd(nodes);
    printMat(nodes);
    printMatNext(nodes);

    int q;
    cin >> q;
    for (int i = 0; i < q; i++)
    {
        int q1, q2;
        cin >> q1 >> q2;
        cout << mat[q1 - 1][q2 - 1] << " " << q1;
        displayRoute(q1 - 1, q2 - 1);
        cout << "-" << q2 << endl;
    }
}