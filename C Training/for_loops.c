#include<stdio.h>
#include<stdlib.h>

int main(){
  for(int i=1; i<=10; ++i){
    printf("%d ",i);
  }
  printf("\n-------------------------------\n");
  int numbers[] = {2,5,4,9,6,8};
  for(int i=0; i<6; ++i){
    printf("%d ",numbers[i]);
  }

  return 0;
}