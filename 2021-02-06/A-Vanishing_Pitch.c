#include <stdio.h>

int main(void)
{
	int v = 0;
	int t_panish = 0;
	int s_appear = 0;
	int d = 0;

	scanf("%d %d %d %d", &v, &t_panish, &s_appear, &d);

	if (d < v * t_panish || v * s_appear < d)
	{
		printf("Yes\n");
		return (0);
	}
	printf("No\n");
	return (0);
}
