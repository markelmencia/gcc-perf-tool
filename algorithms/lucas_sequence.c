#include <stdio.h>

int lucas_sequence(int n){
    if(n == 0){
        return 2;
    }else if(n == 1){
        return 1;
    }else{
        return lucas_sequence(n-1) + lucas_sequence(n-2);
    }
}

int main(){
    printf( lucas_sequence(5000000) );
    
    return 0;
}
