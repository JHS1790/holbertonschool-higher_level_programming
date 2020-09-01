#include "lists.h"
#include <stdio.h>
/**
 * insert_node - inserts node into sorted linked list
 * @head: head of the list to insert into
 * @number: content of new node
 * Return: address of the new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode = malloc(sizeof(listint_t));
	listint_t *prevnode = *head, *nextnode = (*head)->next;

	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	while (nextnode != NULL)
	{
		if (nextnode->n < newnode->n)
		{
			prevnode = nextnode;
			nextnode = nextnode->next;
		}
		else
		{
			if (prevnode == *head)
			{
				newnode->next = *head;
				*head = newnode;
				return (newnode);
			}
			else
			{
				prevnode->next = newnode;
				newnode->next = nextnode;
				return (newnode);
			}
		}
	}
	prevnode->next = newnode;
	newnode->next = nextnode;
	return (newnode);
}
