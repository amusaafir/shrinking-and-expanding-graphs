#ifndef GENERIC_VECTOR_H
	#define GENERIC_VECTOR_H
	#include <stdio.h>	
	#include <stdlib.h>

	typedef struct Vector {
		int max_size;
		void** elements;
		int current_size;
	} vector;

	void init_vector(vector* v);
	void free_vector_elements(vector* v);
	static void double_vector_size(vector* v);
	void add_element_to_vector(vector* v, void* element);
	void* get_element_from_vector(vector* v, int elementIndex);
	int get_size(vector* v);
	
#endif
