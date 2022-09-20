#include<stdio.h>
#include<stdlib.h>

int main(){
    char name[20];
    int age;
    double cgpa;
    printf("Enter your name: ");
    fgets(name,20,stdin); // this inputs a "\n" at the end of the input
    printf("Enter your age: ");
    scanf("%d",&age);
    printf("Enter your CGPA: ");
    scanf("%lf",&cgpa);
    printf("---------------------\n");
    printf("Name: %s",name);
    printf("Age: %d\n",age);
    printf("CGPA: %0.2f\n",cgpa);

    return 0;
}