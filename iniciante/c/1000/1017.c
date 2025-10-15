#include <stdio.h>

int main(){
    int time, speed;
    scanf("%d", &time);
    scanf("%d", &speed);
    printf("%.3lf\n", (time * speed) / 12.0);  
    return 0;
}