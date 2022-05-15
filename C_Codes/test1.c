#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(){
    int i;
    for(int i=0; i<4; i++ )
    {
        fork();
    }
    return 0;
}