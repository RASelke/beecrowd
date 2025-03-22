#include <stdio.h>

int main(){
    char name;
    double fix, sales;
    scanf("%s", &name);
    scanf("%lf", &fix);
    scanf("%lf", &sales);
    printf("TOTAL = R$ %.2lf\n", fix + (sales * 0.15));
    return 0;
}