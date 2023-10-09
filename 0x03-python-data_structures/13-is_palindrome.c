#include "lists.h"

/**
 * is_palindrome - check if list is palindrome
 * @head: head list
 * Return: 0 is not palind or 1
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_palind(head, *head));
}

/**
 * aux_palind - check if list is palind
 * @head: head list
 * @end: end list
 * Return: 0 is not palindrme or 1
 */

int aux_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
