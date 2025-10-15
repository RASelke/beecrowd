#include <stdio.h>

int main(){
    int n1 = 0, n2 = 0, n5 = 0, n10 = 0, n20 = 0, n50 = 0, n100 = 0;
    int number, ini;
    scanf("%d", &number);
    ini = number;

    if(number>=100){
        n100 = number / 100;
        number = number - n100 * 100;
    }
    if(number>=50){
        n50 = number / 50;
        number = number - n50 * 50;
    }
    if(number>=20){
        n20 = number / 20;
        number = number - n20 * 20;
    }
    if(number>=10){
        n10 = number / 10;
        number = number - n10 * 10;
    }
    if(number>=5){
        n5 = number / 5;
        number = number - n5 * 5;
    }
    if(number>=2){
        n2 = number / 2;
        number = number - n2 * 2;
    }
    if(number>=1){
        n1 = number / 1;
        number = number - n1 * 1;
    }

    printf("%d\n", ini);
    printf("%d nota(s) de R$ 100,00\n", n100);
    printf("%d nota(s) de R$ 50,00\n", n50);
    printf("%d nota(s) de R$ 20,00\n", n20);
    printf("%d nota(s) de R$ 10,00\n", n10);
    printf("%d nota(s) de R$ 5,00\n", n5);
    printf("%d nota(s) de R$ 2,00\n", n2);
    printf("%d nota(s) de R$ 1,00\n", n1);
    return 0;
}