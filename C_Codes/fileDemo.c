// #include <stdio.h>
// main()
// {
// FILE *fp;
// char text[ 300];  
// fp=fopen(“file2.txt","r");  
// printf("%s",fgets(text,300,fp));  
//  fclose(fp);
// getch();
// }

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
int main()
{
    FILE *fp;
    char text[300];
    fp = fopen("file2.txt", "r");
    fgets(text, 300, fp);
    printf("%s", text);
    fclose(fp);
    // getch();
    return 0;
}