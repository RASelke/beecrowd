#include <stdio.h>
#include <math.h>

int main(){
    double A, B, C;
    scanf("%lf %lf %lf", &A, &B, &C);
    double delta = B*B - 4 * A * C;
    if(A == 0 || delta < 0){
        printf("Impossivel calcular\n");
    } else{
        printf("R1 = %.5lf\n", ((-B + sqrt(delta)) / (2*A)));
        printf("R2 = %.5lf\n", ((-B - sqrt(delta)) / (2*A)));
    }
    return 0;
}