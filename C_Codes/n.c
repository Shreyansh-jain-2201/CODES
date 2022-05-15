#include <stdio.h>
void test(int *, int *);
int main()
{
    int a = 1, b = 0;
    int c = a % 2 ? a++ : a-- ? a = 0
                      : ++b   ? b = 2
                              : b++;
    printf("%d %d %d\n", a, b, c);
    int i = 4, j = -1, k = 0, w, x, z;
    w = i && j && k;
    x = i || j && k;
    z = i || j && k;
    printf("%d %d %d %d %d %d\n", w, x, z, i, j, k);
    a = 5, b = 6;
    test(&a, &b);
    printf("%d %d\n", a, b);
    return 0;
}

void test(int *p, int *q)
{
    *p = *p * *q;
    *q = *p / *q;
    *p = *p / *q;
}