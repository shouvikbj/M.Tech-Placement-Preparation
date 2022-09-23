#include<stdio.h>
#include<stdlib.h>

int main(){
  int secret=21;
  int guess;
  int guess_count=5;
  printf("The secret number is an integer between 1 and 100.\n");
  printf("You have 5 guesses.\n");
  printf("What is your guess? : ");
  scanf("%d",&guess);
  while(guess!=secret && guess_count>1){
    guess_count -= 1;
    printf("Wrong guess !\n");
    if(guess_count==1){
     printf("%d guess left..\n", guess_count);
    }
    else{
      printf("%d guesses left..\n", guess_count);
    }
    printf("\nYour next guess? :");
    scanf("%d",&guess);
  }
  if(guess==secret){
    printf("\nYay! you guessed right !!!\n");
  }
  else if(guess_count==1){
    printf("\nSorry! You ran out of guesses..\n");
  }
  return 0;
}