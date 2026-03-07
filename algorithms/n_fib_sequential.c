#include <stdio.h>

long n_fib_sequential(long n) {
  
    if (n <= 1) {
        return n;
	}

    long a = 0, b = 1;

    for (long i = 2; i <= n; i++) {
        long c = a + b;
        a = b;
        b = c;
    }
    return b;
}

int main() {
	printf("%lu\n", n_fib_sequential(5000000000));
	return 0;
}
