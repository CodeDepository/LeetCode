int ispalindrome(char *string) { //or char string[]
	int left = 0;
	int right = strlen(string);

	
	while (1) {
		while (left < right && is_space(string[left])) {
			++left;
		}
		while (left < right && is_space(string[right])) {
			--right;
		}
		if (left >= right) {
			return 1;
		}
		else if (string[left] != string[right]) {
			return 0;
		}
		++left;
		--right;
	}
	return 0;
}
