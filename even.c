#include<stdio.h>
void main()
{
  double int a;
  scanf("%ld",&a);
  if(a<0)
      printf("invalid");
  else if(a%2==0)
      printf("Even");
  else
      printf("Odd");
      
}
