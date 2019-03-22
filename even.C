#include<stdio.h>
void main()
{
  int a;
  scanf("%d",&a);
  if(a<0)
    printf("invalid");
  else if(a%2==0)
    printf("Even");
  else
    print("Odd");
}
