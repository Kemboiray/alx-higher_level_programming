#include "lists.h"

/**
 * print_dlistint - prints all the elements of a dlistint_t list
 * @h: pointer to head node
 *
 * Return: number of nodes printed
 */
size_t print_dlistint(const dlistint_t *h)
{
	dlistint_t *temp = (dlistint_t *)h;
	size_t n = 0;

	while (temp)
	{
		printf("%d\n", temp->n);
		temp = temp->next;
		n++;
	}

	return (n);
}
