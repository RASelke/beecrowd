#include <stdio.h>

int main(){
    int N;
    int horas = 0, minutos = 0, segundos = 0;
    scanf("%d", &N);
    if(N >= 3600){
        horas = N / 3600;
        N = N - horas * 3600;
    }
    if(N >= 60){
        minutos = N / 60;
        N = N - minutos * 60;
    }
    segundos = N;
    printf("%d:%d:%d\n", horas, minutos, segundos);
    return 0;
}