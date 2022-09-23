#include<stdio.h>
#include<stdlib.h>

int main(){
  char line[255];
  FILE* file_pointer = fopen("employees.txt", "r");

  for(int i=0; i<3; ++i){
    fgets(line, 255, file_pointer);
    printf("%s \n", line);
  }

  fclose(file_pointer);
  return 0;
}