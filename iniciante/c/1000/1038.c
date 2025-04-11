#include <stdio.h>

int main(){
    int codigo, quantidade;
    double valor;
    scanf("%d %d", &codigo, &quantidade);
    if(codigo == 1){
        valor = quantidade * 4.0;
    } else if (codigo == 2){
        valor = quantidade * 4.5;
    } else if (codigo == 3){
        valor = quantidade * 5.0;
    } else if (codigo == 4){
        valor = quantidade * 2.0;
    } else if (codigo == 5){
        valor = quantidade * 1.5;
    }

    printf("Total: R$ %.2lf\n", valor);
    
    return 0;
}