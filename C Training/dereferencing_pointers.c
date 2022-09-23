#include<stdio.h>
#include<stdlib.h>

int main(){
  int age=40;
  int* pAge = &age;

  printf("%d -> %p \n",*pAge,pAge);

  printf("%d \n", *&age);
  
  return 0;
}