#include <stdio.h>
#include <stdlib.h>

int main()
{
  // int luckyNumbers[] = {4, 8, 15, 16, 23, 42};
  // printf("%d \n", luckyNumbers[0]);
  // printf("%d \n", luckyNumbers[2]);

  // printf("%d \n", luckyNumbers[1]);
  // luckyNumbers[1] = 55;
  // printf("%d \n", luckyNumbers[1]);

  // printf("All elements of the array are...\n");
  // for (int i = 0; i < 6; ++i)
  // {
  //   printf("Index %d: %d\n", i, luckyNumbers[i]);
  // }

  int luckyNumbers[10];
  for (int i = 0; i < 10; ++i)
  {
    luckyNumbers[i] = (i + 1);
  }
  printf("All elements of the array are...\n");
  for (int i = 0; i < 10; ++i)
  {
    printf("Index %d: %d\n", i, luckyNumbers[i]);
  }

  return 0;
}