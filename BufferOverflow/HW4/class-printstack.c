#include <stdio.h>

void function(int a, int b, int c)
{
	char buffer1[10];
	char buffer2[18];
	int *ret, i;

	for(i=0;i<10;i++) buffer1[i]=i;
	for(i=0;i<18;i++) buffer2[i]=i;

	ret=(int *)buffer2;
	for(i=22;i>=0;i--) printf("%8X : %8X\n", &(ret[i]),ret[i]);
}

int main() {
	function(1,2,3);
}
