#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

int binarySearch(int arr[], int target, int start, int end);
void arrayPrinter(int arr[], int arrayLen);

int main(void) {
	int arr[9] = { 12, 34, 37, 45, 57, 82, 99, 120, 134 };
	int target;
	int start = 0;
	int end = (sizeof(arr) / sizeof(int)) - 1;

	arrayPrinter(arr, sizeof(arr) / sizeof(int));

	printf("Target Integer : ");
	scanf_s("%d", &target);

	int k = binarySearch(arr, target, start, end);

	printf("target found : %d", k);

}

int binarySearch(int arr[], int target, int start, int end) {
	int centre = (end + start) / 2;
	
	if (arr[centre] == target)
		return arr[centre];

	else if (arr[centre] < target) {
		return binarySearch(arr, target, centre + 1, end);
	}
	else if (arr[centre] > target) {
		return binarySearch(arr, target, start, centre - 1);
	}
	else;

}

void arrayPrinter(int arr[], int arrayLen) {
	printf("Current Array : [ ");
	for (int i = 0; i < arrayLen; i++) {
		printf("%d ", *(arr + i));
	}
	printf("]\n\n");
}