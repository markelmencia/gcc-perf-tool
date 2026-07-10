#include <stdio.h>

static inline int prueba_overhead(int n){
    return n + 1;
}

int main(){
    int a = 0;
    for(int i = 0; i < 1000000000; i++){
        a += prueba_overhead(1);
    }

    printf("%d", a);
    
}
