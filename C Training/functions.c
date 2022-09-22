#include <stdio.h>
#include <stdlib.h>

int power(int num, int pow);

int main()
{
  int result = power(2, 3);
  printf("%d\n", result);

  return 0;
}

int power(int num, int pow)
{
  int res = 1;
  if (pow == 0)
  {
    return res;
  }
  for (int i = 0; i < pow; ++i)
  {
    res *= num;
  }
  return res;
}