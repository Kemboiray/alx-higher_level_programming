#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: address of pointer to beginning of the list
 * @number: number to be inserted
 *
 * Return: address of new node (success) or NULL (failure)
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp;

	if (*head == NULL)
	{
		new = add_nodeint_end(head, number);
		return (new);
	}

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;
	temp = *head;

	while (temp->next)
	{
		if (number > temp->n && number < temp->next->n)
		{
			new->next = temp->next;
			break;
		}
		temp = temp->next;
	}

	temp->next = new;
	return (new);
}
