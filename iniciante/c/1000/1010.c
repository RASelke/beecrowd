#include <stdio.h>

int main(){
    int code, numb, code2, numb2;
    double value, value2;
    scanf("%d %d %lf", &code, &numb, &value);
    scanf("%d %d %lf", &code2, &numb2, &value2);
    printf("VALOR A PAGAR: R$ %.2lf\n", (numb * value) + (numb2 * value2));
    return 0;
}