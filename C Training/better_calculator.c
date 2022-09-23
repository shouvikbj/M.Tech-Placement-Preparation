#include <stdio.h>
#include <stdlib.h>

double calculate(double num1, char op, double num2){
  if(op=='+'){
    return (num1+num2);
  }
  else if(op=='-'){
    return (num1-num2);
  }
  else if(op=='*'){
    return (num1*num2);
  }
  else if(op=='/'){
    return (num1/num2);
  }
  else{
    return -1;
  }
}

int main()
{
  double num1,num2;
  char op;
  
  printf("Enter first number: ");
  scanf("%lf",&num1);

  printf("Enter operator ( + or - or * or / ): ");
  scanf(" %c",&op);

  printf("Enter second number: ");
  scanf("%lf",&num2);

  double result = calculate(num1,op,num2);

  if(result==-1){
    printf("Invalid operation!");
  }
  else{
    printf("Result: { (%0.2f %c %0.2f) = %0.2f }",num1,op,num2,result);
  }

  return 0;
}