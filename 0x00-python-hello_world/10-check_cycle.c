#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to list
 *
 * Return: 1 (cycle is found), or 0 (cycle is not found).
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;

	if (!list)
		return (0);
	temp = list;
	while (temp)
	{
		if (temp->next == list)
			return (1);
		temp = temp->next;
	}
	return (0);
}
