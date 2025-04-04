#include <stdio.h>

int main(){
    int cedulas[] = {10000, 5000, 2000, 1000, 500, 200};
    int moedas[] = {100, 50, 25, 10, 5, 1};
    int reais, centavos;

    scanf("%d.%d", &reais, &centavos);
    reais = reais * 100 + centavos;

    printf("NOTAS:\n");
    for (int i = 0; i < 6; i++){
        printf("%d nota(s) de R$ %.2lf\n", reais / cedulas[i], cedulas[i] / 100.0);
        reais = reais % cedulas[i];
    }

    printf("MOEDAS:\n");
    for (int i = 0; i < 6; i++){
        printf("%d moeda(s) de R$ %.2lf\n", reais / moedas[i], moedas[i] / 100.0);
        reais = reais % moedas[i];
    }

    return 0;
}