#include<stdio.h>
#include<stdlib.h>

int main(){
    double first,second;
    printf("Enter first number: ");
    scanf("%lf",&first);
    printf("Enter second number: ");
    scanf("%lf",&second);
    double sum=first+second;
    printf("Sum of %0.2f and %0.2f is: %0.2f \n",first,second,sum);

    return 0;
}