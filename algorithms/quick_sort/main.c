#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b);
int* load_array(const char* filename, int* n_items);

int main() {
    int n_items;
    int* array = load_array("data.txt", &n_items);

    if (array == NULL) {
        return 1;
    }

    qsort(array, n_items, sizeof(int), compare);

    for (int i = 0; i < n_items; i++) {
        printf("%d ", array[i]);
    }

    printf("\n");

    free(array);
    return 0;
}

int* load_array(const char* filename, int* n_items) {
    FILE* fptr = fopen(filename, "r");
    if (!fptr) {
        perror("Error abriendo archivo");
        return NULL;
    }

    if (fscanf(fptr, "%d,", n_items) != 1) {
        perror("Error leyendo tamaño");
        fclose(fptr);
        return NULL;
    }

    int* arr = malloc((*n_items) * sizeof(int));
    if (!arr) {
        perror("Error reservando memoria");
        fclose(fptr);
        return NULL;
    }

    for (int i = 0; i < *n_items; i++) {

        if (i < *n_items - 1) {
            if (fscanf(fptr, "%d,", &arr[i]) != 1) {
                perror("Error leyendo dato");
                free(arr);
                fclose(fptr);
                return NULL;
            }
        } else {
            if (fscanf(fptr, "%d;", &arr[i]) != 1) {
                perror("Error leyendo último dato");
                free(arr);
                fclose(fptr);
                return NULL;
            }
        }
    }

    fclose(fptr);
    return arr;
}

int compare(const void* a, const void* b) {
    int valA = *(const int*)a;
    int valB = *(const int*)b;
    return valA - valB;
}
