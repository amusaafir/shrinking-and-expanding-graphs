#include "generic_vector.h"

void init_vector(vector* v) {
	const int INITIAL_VECTOR_SIZE = 5;
	v->max_size = INITIAL_VECTOR_SIZE;
	v->elements = (void**) malloc(sizeof(void*) * INITIAL_VECTOR_SIZE);
	v->current_size = 0;
}

void free_vector_elements(vector* v) {
	free(v->elements);
}

static void double_vector_size(vector* v) {
	const int RESIZE_SCALE = 2;
	void** elements = realloc(v->elements, sizeof(void*) * (v->max_size * RESIZE_SCALE));
	v->elements = elements;
	v->max_size *= RESIZE_SCALE;
}

void add_element_to_vector(vector* v, void* element) {
	if (v->current_size == v->max_size) {
		double_vector_size(v);
	}

	v->elements[v->current_size] = element;
	v->current_size++;
}

void* get_element_from_vector(vector* v, int element_index) {
	if (element_index >= v->current_size) {
		printf("Requested element out of bounds from current vector size.");
		return NULL;
	}

	return v->elements[element_index];
}

int get_size(vector* v) {
	return v->current_size;
}