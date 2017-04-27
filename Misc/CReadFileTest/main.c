#include "main.h"

const char* SOURCE_FILE = "C:/Users/AJ/Desktop/somerandomfile.txt";

void print_file(FILE* file) {
	while (1) {
		int character = fgetc(file);

		if (feof(file)) {
			break;
		}

		printf("%c", character);
	}
}

FILE* open_file() {
	return fopen(SOURCE_FILE, "r");
}

int main() {

	/*FILE* file = open_file();
	
	if (file == NULL) {
		printf("Error opening file.");
		
		return 0;
	}

	print_file(file);

	fclose(file);
	*/
	
	// Create a vector
	vector v;
	init_vector(&v);

	// Add a number to the vector
	int age = 24;
	add_element_to_vector(&v, &age);

	// Get the first number and print it.
	int* element = get_element_from_vector(&v, 0);
	printf("%d", *element);
	
	free_vector_elements(&v);

	return 0;
}
