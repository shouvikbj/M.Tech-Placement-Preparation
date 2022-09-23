#include<stdio.h>
#include<stdlib.h>

int main(){
  int age=30;
  double gpa=9.62;
  char grade='A';

  printf("%d -> %p \n",age,&age);
  printf("%0.2f -> %p \n",gpa,&gpa);
  printf("%c -> %p \n",grade,&grade);
  
  return 0;
}