#include<stdio.h>
#include<stdlib.h>

int main(){
  FILE* file_pointer = fopen("employees.txt","w");

  fprintf(file_pointer, "Shouvik Bajpayee, Avionics Software Engineer, Airbus, 20 LPA\n");
  fprintf(file_pointer, "Shouvik Bajpayee, Assistant System Engineer, TCS, 7.5 LPA\n");

  fclose(file_pointer);

  
  FILE* file_pointer2 = fopen("employees.txt","a");

  fprintf(file_pointer2, "Satadal Banerjee, Big Data Engineer, Micron, 20 LPA\n");
  
  fclose(file_pointer2);

  return 0;
}