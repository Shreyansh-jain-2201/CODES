// Build windows 2000 skeleton using graphics.h in C programming
#include <stdio.h>
#include <stdlib.h>
#include <graphics.h>

int main()
{
    int gd = DETECT, gm;
    initgraph(&gd, &gm, (char *)"");
    circle(100, 100, 50);
    getch();
    closegraph();
    return 0;
}