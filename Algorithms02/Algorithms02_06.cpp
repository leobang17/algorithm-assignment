#define _CRT_SECURE_NO_WARNIGNS
#include <stdio.h>

void pairSum(int arr[], int targetNum, int arrayLen);
void printerArray(int arr[], int arrayLen);
void printerFunc(int firstNum, int secondNum, int count);

int main() {
	int numArray[10] = { 2, 4, 3, 5, 6, -2, 4, 7, 8, 9 };
	int targetNum = 7;

	printerArray(numArray, sizeof(numArray) / sizeof(int));
	
	pairSum(numArray, targetNum, sizeof(numArray) / sizeof(int));
}

void pairSum(int arr[], int targetNum, int arrayLen) {
	printf("Pairs: ");
	printf("[ ");
	int count = 0;
	for (int firstIndex = 0, secondIndex = 1; firstIndex < arrayLen - 1; firstIndex++, secondIndex++) {
		for (int p = secondIndex; p < arrayLen; p++) {
			if (arr[firstIndex] + arr[p] == targetNum) {
				printerFunc(arr[firstIndex], arr[p], count);	
				count++;
			}
			else;			
		}
	}
	printf(" ]");
}


void printerFunc(int firstNum, int secondNum, int count) {
	if (count == 0) printf("'%d + %d'", firstNum, secondNum);
	else printf(", '%d + %d'", firstNum, secondNum);
}

void printerArray(int arr[],int arrayLen) {
	printf("Components: ");
	printf("[ ");
	for (int i = 0; i < arrayLen; i++) {
		if (i != arrayLen - 1)
			printf("%d, ", *arr + i);
		else
			printf("%d", arr[i]);
	}
	printf(" ]");
	printf("\n\n");
}