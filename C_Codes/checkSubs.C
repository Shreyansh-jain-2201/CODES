#include <stdio.h>
#include <string.h>

int checkSubs(char *str, char *substr, int l, int l1)
{
    int ind = l - l1;
    int flag = 0;
    int i, j;
    for (i = 0; i <= ind; i++)
    {
        for (j = 0; j < l1; j++)
        {
            if (str[i + j] != substr[j])
                break;
        }
        if (j == l1)
        {
            flag = 1;
            break;
        }
    }
    if (flag)
        return i;
    else
        return -1;
}
int main()
{
    char str[1000], substr[1000];
    int l = 0, l1 = 0;
    fgets(str, sizeof str, stdin);
    fgets(substr, sizeof substr, stdin);
    while (str[l] != '\0')
        l++;
    l--;

    while (substr[l1] != '\0')
        l1++;
    l1--;
    int index = checkSubs(str, substr, l, l1);
    printf("%d", index);
    return 0;
}

// // int checkSubs(char str[100],)

// #include <stdio.h>
// int main()
// {
//     char str[80], subs[20];
//     int c1 = 0, c2 = 0, i, j, flg;
//     fgets(str, sizeof str, stdin);
//     fgets(subs, sizeof subs, stdin);

//     while (str[c1] != '\0')
//         c1++;
//     c1--;

//     while (subs[c2] != '\0')
//         c2++;
//     c2--;

//     for (i = 0; i <= c1 - c2; i++)
//     {
//         for (j = i; j < i + c2; j++)
//         {
//             flg = 1;
//             if (str[j] != subs[j - i])
//             {
//                 flg = 0;
//                 break;
//             }
//         }

//         if (flg == 1)

//             break;
//     }
//     if (flg == 1)
//         printf("%d", i);
//     else
//         printf("-1");
//     return 0;
// }