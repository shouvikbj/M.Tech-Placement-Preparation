#include<stdio.h>
#include<stdlib.h>

int main(){
    int num=10;
    printf("%d\n",num);

    num=5;
    printf("%d\n",num);

    const int NUM=20; // this variable cannot be changed
    printf("%d\n",NUM);
    // NUM=5; // this cannot be done
    // printf("%d\n",NUM);

    return 0;
}