#include <stdio.h> 
#include <stdlib.h> 
#include <errno.h> 
#include <string.h> 
#include <setjmp.h> 

int arr[10] = {10, 20, 30, 40, -50, 60, -70, 80, -90, 100}; 
jmp_buf buffer; 

void f1 (int x); 
void f2 (int x); 
void f3 (int x); 

int main (void) 
{
	int i, ret; 

	i = 0; 
	while (i < 10)
	{

		ret = setjmp (buffer); 
		if (ret == 0)
		{
			printf ("Jump location is set\n"); 
		}
		if (ret == 1) 
		{
			printf ("sorry for the negative int\n"); 
			i++; 
			continue; 
		}

		f1 (arr[i]); 
		i++; 
	}
}

void f1 (int x)
{
	f2 (x); 
}

void f2 (int x)
{
	f3 (x); 
}

void f3 (int x)
{
	if (x < 0) 
	{
		longjmp (buffer, 1); 
	}
}
