#include "lists.h"

/**
 * is_palindrome - checks whether a linked list is a palindrome
 * @head: Address of pointer to the head of the linked list
 *
 * Return: 1 (true), 0 (false) or -1 (memory allocation failure).
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int *arr = NULL;
	unsigned int len, i;

	if (temp == NULL)
		return (1);

	for (len = 0; temp; len++, temp = temp->next)
		;

	arr = malloc(len * sizeof(int));
	if (arr == NULL)
		return (-1);

	for (i = 0, temp = *head; temp; i++, temp = temp->next)
		arr[i] = temp->n;

	for (i = 0; i < len / 2; i++)
	{
		if (arr[i] != arr[len - 1 - i])
		{
			free(arr);
			return (0);
		}
	}

	free(arr);
	return (1);
}
