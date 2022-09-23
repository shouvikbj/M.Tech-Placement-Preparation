#include<stdio.h>
#include<stdlib.h>

int main(){
  int age=30;
  int* pointer = &age;

  printf("%d -> %p \n",age,&age);
  printf("%d -> %p \n",*pointer,pointer);
  
  return 0;
}