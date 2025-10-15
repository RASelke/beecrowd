#include <stdio.h>

int main(){
    int n2 = 0, n5 = 0, n10 = 0, n20 = 0, n50 = 0, n100 = 0;
    int m1 = 0, m05 = 0, m025 = 0, m010 = 0, m005 = 0, m001 = 0;
    double number;
    scanf("%lf", &number);

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
    printf("NOTAS:\n");
    printf("%d nota(s) de R$ 100.00\n", n100);
    printf("%d nota(s) de R$ 50.00\n", n50);
    printf("%d nota(s) de R$ 20.00\n", n20);
    printf("%d nota(s) de R$ 10.00\n", n10);
    printf("%d nota(s) de R$ 5.00\n", n5);
    printf("%d nota(s) de R$ 2.00\n", n2);
    
    if(number>=1){
        m1 = number / 1.0;
        number = number - m1 * 1.0;
    }
    if(number>=0.5){
        m05 = number / 0.5;
        number = number - m05 * 0.5;
    }
    if(number>=0.25){
        m025 = number / 0.25;
        number = number - m025 * 0.25;
    }
    if(number>=0.1){
        m010 = number / 0.1;
        number = number - m010 * 0.1;
    }
    if(number>=0.05){
        m005 = number / 0.05;
        number = number - m005 * 0.05;
    }
    if(number>=0.01){
        m001 = number / 0.01;
        number = number - m001 * 0.01;
    }
        printf("MOEDAS:\n");
        printf("%d moeda(s) de R$ 1.00\n", m1);
        printf("%d moeda(s) de R$ 0.50\n", m05);
        printf("%d moeda(s) de R$ 0.25\n", m025);
        printf("%d moeda(s) de R$ 0.10\n", m010);
        printf("%d moeda(s) de R$ 0.05\n", m005);
        printf("%d moeda(s) de R$ 0.01\n", m001);
    return 0;
}