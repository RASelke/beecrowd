#include <stdio.h>

int main(){
    int numb, time;
    double value;
    scanf("%d", &numb);
    scanf("%d", &time);
    scanf("%lf", &value);
    printf("NUMBER = %d\n", numb);
    printf("SALARY = U$ %.2lf\n", time * value);
    return 0;
}