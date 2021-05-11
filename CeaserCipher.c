#include<stdio.h>
#include<string.h>

int main()
{
    int k,m,n;
    char str[1000];
    printf("Enter the string to be encrytpted:");
    scanf("%s",str);
    m=strlen(str);

    printf("Enter the key to shift:");
    scanf("%d",&k);
    k=k%26;
    for (int i=0;i<m;i++)
    {
        n=str[i];
        if (n>=97&&n<=122)
        {
            n=n+k;
            if(n>122)
            {
                printf("%c",n-26);
            }
            else
            {
                printf("%c",n);
            }
        }
        else if (n>=65&&n<=90)
        {
            n=n+k;
            if(n>90)
            {
                printf("%c",n-26);
            }
            else
            {
                printf("%c",n);
            }
        }  
    }
    return 0;
}