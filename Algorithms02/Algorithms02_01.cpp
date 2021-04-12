#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// program: display the largest k (positive int) that satisfies f: 2^k <= n
// display the results for three n's = {10, 50, 1025}

int powFunc(int k);

int main(void) {
	int n[3] = { 10, 50, 1025 };

	for (int i = 0; i < 3; i++) {
		int k = 1;

		for (int j = 0; ; j++) {
			if (powFunc(k) <= n[i]) {
				k++;
			}
			else {
				printf("The Largest K satisfying 2^K <= %d is : %d\n\n", n[i], k - 1);
				break;
			}
		}		
	}
}

int powFunc(int k) {
	int pow = 1;
	for (int i = 0; i < k; i++) {
		pow *= 2;
	}
	return pow;
}