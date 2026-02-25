#include <stdio.h>
#include <stdlib.h>

int* generate_random_array(int length, int max_num) {
	int *result = malloc(length * sizeof(int));
	for (int i = 0; i < length; i++) {
		result[i] = rand() % 100 + 1;
	}
	return result;
}

void bubble_sort(int num_array[], int length) {
    int done;
    for (int i = 0; i < length - 1; i++) {
        done = 1;
        for (int j = 0; j < length - i - 1; j++) {
            if (num_array[j] > num_array[j + 1]) {
				int tmp = num_array[j];
				num_array[j] = num_array[j + 1];
				num_array[j + 1] = tmp;
                done = 0;
            }
        }

        if (done == 1) {
            break;
		}
    }
}

int main() {
	srand(0);
	int *nums = generate_random_array(100, 100);
	bubble_sort(nums, 100);
	for (int i = 0; i < 100; i++) {
		printf("%d\n", nums[i]);
	}
}

