#include <stdio.h>
int main()
{
    int m,key_asc;
    printf("Enter the key:");
    char k[1];
    scanf("%s",k);
    key_asc=k[0];
    char str[100];
    printf("Enter the string :");
    scanf("%s",str);
    printf("Encrypted string :");
    for(int i=0;str[i];i++)
    {
        printf("%c ",str[i]^key_asc);
    }
}