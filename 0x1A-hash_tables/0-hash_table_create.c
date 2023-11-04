#include "hash_tables.h"

/**
 * hash_table_create - a function that creat hash table
 *
 * @size: takes a size of hash table as input
 *
 * Return: pointer to hash table or 0 in error
 */

hash_table_t *hash_table_create(unsigned long int size)
{
	unsigned long int i;

	hash_table_t *hash_table;

	hash_table = malloc(sizeof(hash_table_t));

	if (!hash_table)
		return (NULL);

	hash_table->size = size;
	hash_table->array = malloc(sizeof(hash_table_t));
	if (!hash_table->array)
	{
		free(hash_table);
		return (NULL);
	}
	for (i = 0; i < size; i++)
	{
		hash_table->array[i] = NULL;
	}
	return (hash_table);
}
