#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isEven(int num)
{
  if (num % 2 == 0)
  {
    return true;
  }
  else
  {
    return false;
  }
}

int main()
{
  int num;
  printf("Enter a number: ");
  scanf("%d", &num);
  if (isEven(num))
  {
    printf("Even number\n");
  }
  else
  {
    printf("Odd number\n");
  }
  return 0;
}