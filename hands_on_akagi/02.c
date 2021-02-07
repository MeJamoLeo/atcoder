#include <stdio.h>

int main(void)
{
	int n = 0;
	int i = 0;
	int s_max_time = 0;
	int d_min_damege = 0;

	scanf("%d %d %d", &n, &s_max_time, &d_min_damege);
	scanf()

	int x_time[n];
	int y_damege[n];

	while (i < n)
	{
		scanf("%d %d", &x_time[i], &y_damege[i]);
		i++;
	}

	i = 0;
	while (i < n)
	{
		if (x_time[i] < s_max_time && y_damege[i] < d_min_damege)
		{
			printf("Yes\n");
			return (0);
		}
		i++;
	}

	printf("No\n");
	return (0);
}
