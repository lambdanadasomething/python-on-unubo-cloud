#include <stdio.h>

int main(int argc, char **argv)
{
    if (argc <= 1)
        printf("Hello world, guest!\n");
    else
        printf("Hello world, %s!\n", argv[1]);
    
    return 0;
}