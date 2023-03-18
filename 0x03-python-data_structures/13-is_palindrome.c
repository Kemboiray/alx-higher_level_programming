#include "lists.h"

/**
 * is_palindrome - checks whether a linked list is a palindrome
 * @head: Address of pointer to the head of the linked list
 *
 * Return: 1 (true) or 0 (false).
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	unsigned int len, i;

	if (temp == NULL)
		return (1);

	for (len = 0; temp; len++, temp = temp->next)
		;

	int arr[len];

	for (i = 0, temp = *head; temp; i++, temp = temp->next)
		arr[i] = temp->n;

	for (i = 0; i < len / 2; i++)
	{
		if (arr[i] != arr[len - 1 - i])
			return (0);
	}

	return (1);
}
