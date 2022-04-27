// Implement the following with and without library function:	
// Use graphic.h to draw a rectangle
// Use graphic.h to draw a circle
// Use graphic.h to draw a line
// Draw a line provided two points	
// Draw a circle provided point and radius	
// Draw a rectangle

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <graphic.h>

int main()
{
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "C:\\TC\\BGI");
    int i;
    // Draw a line
    line(0, 0, getmaxx(), getmaxy());
    // Draw a circle
    circle(getmaxx() / 2, getmaxy() / 2, 100);
    // Draw a rectangle
    rectangle(0, 0, getmaxx(), getmaxy());
    // Draw a line provided two points
    line(0, 0, getmaxx(), getmaxy());
    // Draw a circle provided point and radius
    circle(getmaxx() / 2, getmaxy() / 2, 100);
    // Draw a rectangle
    rectangle(0, 0, getmaxx(), getmaxy());
    getch();
    closegraph();
    return 0;
}