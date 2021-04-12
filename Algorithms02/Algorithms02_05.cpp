#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int * matrixCreator(void);
void rotator(int* arr[5][5]);
void matrixViewer(int* array[5][5]);

int main(void){
	srand((unsigned)time(NULL));
	
	int* arrptr[5][5] = { 0 };
	int* ptr = matrixCreator();
	
	// mapping pointer values to 2 dimensional array.
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5; j++) {
			arrptr[i][j] = ptr + i * 5 + j;
		}
	}

	// print original matrix
	printf("Original Matrix\n\n");
	matrixViewer(arrptr);

	printf("--------------------------------------------------------\n");

	// rotate the matrix and print clock wise rotated matrix
	printf("Rotated Matrix\n\n");
	rotator(arrptr);

}

int* matrixCreator(void) {
	static int matrix[5][5] = {0};

	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5; j++) {
			matrix[i][j] = rand() % 2;
		}
	}

	return (int *) matrix;
}

void rotator(int * arr[5][5]) {
	int* tempptr[5][5] = { 0 };
	int column = 5, row = 5;

	for (int i = 0; i < row ; i++) {
		for (int j = 0; j < column; j++) {
			tempptr[i][j] = arr[row - 1 - j][i];
		}
	}

	matrixViewer(tempptr);
 		
}

void matrixViewer(int* array[5][5]) {
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5; j++) {
			printf("%d ", *array[i][j]);
		}
		printf("\n\n");
	}
}