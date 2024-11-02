#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Creates an infinite loop
 * Description: Function that keeps the program running
 * Return: Always 0 (Success)
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates 5 zombie processes
 * Description: Program that demonstrates zombie process creation
 * Return: Always 0 (Success)
 */
int main(void)
{
	pid_t zombie_pid;
	unsigned int i;

	for (i = 0; i < 5; i++)
	{
		zombie_pid = fork();
		if (zombie_pid < 0)
		{
			perror("fork");
			return (1);
		}
		if (zombie_pid == 0)
		{
			exit(0);
		}
		else
		{
			printf("Zombie process created, PID: %d\n", zombie_pid);
		}
	}

	infinite_while();
	return (0);
}
