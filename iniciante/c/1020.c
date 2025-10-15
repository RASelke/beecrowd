#include <stdio.h>

int main(){
    int N;
    int ano = 0, mes = 0, dia = 0;
    scanf("%d", &N);
    if(N >= 365){
        ano = N / 365;
        N = N - ano * 365;
    }
    if(N >= 30){
        mes = N / 30;
        N = N - mes * 30;
    }
    dia = N;
    printf("%d ano(s)\n", ano);
    printf("%d mes(es)\n", mes);
    printf("%d dia(s)\n", dia);
    return 0;
}