#include "lists.h"
/**
 * check_cycle - checks if the linked list is cycling
 * @list: list we're checking
 * Return: 0 if no cycle, 1 if yes
 */
int check_cycle(listint_t *list)
{
	listint_t *addresses[1024];
	int i, j = 0;

	while (list->next != NULL)
	{
		addresses[j] = list;
		for (i = 0; i <= j; i++)
		{
			if (list->next == addresses[i])
				return (1);
		}
		j++;
		list = list->next;
	}
	return (0);
}
