# define _CRT_SECURE_NO_WARNINGS
# include <stdio.h>
# include <string.h>

// write a function determines if the given word is palindrome or not.
// Disply the results when you put two different words (one is palindrome / the other is not.)

void determiner(int wordLen, char word[50]);

int main(void) {
	char exitCommand[5] = "exit";
	while (1) {
		char word[50] = "\0";

		printf("input word : ");
		gets_s(word, 50);
		if (strcmp(word, exitCommand) == 0) {
			printf("\nExit Program");
			break;
		}

		int wordLen = strlen(word);

		determiner(wordLen, word);

	}
}

void determiner(int wordLen, char word[50]) {
	int p = 0;
	for (int i = 0; i < (wordLen / 2); i++) {
		if (word[i] == word[wordLen - 1 - i]) {
			p++;
		}
		else;		
	}
	if (p == wordLen / 2) {
		printf("%s is a palindrome\n\n", &word[0]);
	}
	else {
		printf("%s is not a palindrome\n\n", &word[0]);
	}
}