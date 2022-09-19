#include <stdio.h>
#include <stdlib.h>

int main()
{
    char name[] = "George";
    // char name[] = "John";

    int age = 70;
    // int age = 35;

    printf("There once was a man named %s.\n", name);
    printf("He was %d years old.\n", age);
    printf("He really liked the name %s.\n", name);
    printf("But he did not like being %d.\n", age);

    return 0;
}