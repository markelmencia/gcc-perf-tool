#include <stdio.h>

int n_fib_recursive(int n) {
    if (n <= 1){
        return n;
    }
    
    return n_fib_recursive(n - 1) + n_fib_recursive(n - 2);
}

int main() {
	printf("%d\n", n_fib_recursive(42));
	return 0;
}

