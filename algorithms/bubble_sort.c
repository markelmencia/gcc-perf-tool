#include <stdio.h>

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
	int nums[] = {3, 5, 2, 2, 1, 7, 9, 2, 4, 5};
	bubble_sort(nums, 10);
	for (int i = 0; i < 10; i++) {
		printf("%d\n", nums[i]);
	}
}

