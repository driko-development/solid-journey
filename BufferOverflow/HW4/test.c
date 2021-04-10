#include <stdio.h>

#ifndef FOO
#define FOO 0
#endif

#ifndef BAR
#define BAR 0
#endif

void function (int a, int b, int c) 
{
	char buffer1[10];
	char buffer2[18];
	int *ret, i;
	ret = buffer2+FOO;
	(*ret)+=BAR;
}

int main() 
{
	int x, y;
	x=0;
	y=0;
	function(1,2,3);
	x=1;
	y=2;
	printf("%d %d\n",x,y);
}
