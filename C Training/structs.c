#include<stdio.h>
#include<stdlib.h>
#include<string.h>

struct Student{
  char name[50];
  char major[50];
  int age;
  double gpa;
};

int main(){
  struct Student student1;
  strcpy(student1.name, "Shouvik Bajpayee");
  student1.age = 22;
  strcpy(student1.major, "Distributed and Mobile Computing");
  student1.gpa = 9.62;

  printf("Student Details...\n\n");
  printf("Name: %s\n",student1.name);
  printf("Age: %d\n",student1.age);
  printf("Major: %s\n",student1.major);
  printf("CGPA: %0.2f\n",student1.gpa);

  return 0;
}