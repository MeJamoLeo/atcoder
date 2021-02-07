#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int		is_sep(char x, char *charset)
{
	int i;

	i = 0;
	if (x == '\0')
		return (1);
	while (charset[i] != '\0')
	{
		if (charset[i] == x)
			return (1);
		i++;
	}
	return (0);
}

int		get_ary_len(char *str, char *charset)
{
	int i;
	int k;

	i = 0;
	k = 0;
	while (str[i] != '\0')
	{
		if (!is_sep(str[i], charset) &&
			is_sep(str[i + 1], charset))
			k++;
		i++;
	}
	return (k);
}

char	*ft_strncpy(char *dest, char *src, unsigned int n)
{
	unsigned int		index;

	index = 0;
	while (index < n && src[index] != '\0')
	{
		dest[index] = src[index];
		index++;
	}
	while (index < n)
	{
		dest[index] = '\0';
		index++;
	}
	dest[index] = '\0';
	return (dest);
}

char	**fill_ary(char *str, char **heap, char *charset)
{
	int i;
	int j;
	int k;

	i = 0;
	k = 0;
	while (str[i] != '\0')
	{
		j = i;
		if (is_sep(str[i], charset))
		{
			i++;
			j = i;
		}
		else
		{
			while (!is_sep(str[j], charset))
				j++;
			heap[k] = (char *)malloc(sizeof(char) * (j - i + 1));
			ft_strncpy(heap[k], &str[i], j - i);
			i = j;
			k++;
		}
	}
	return (heap);
}

char	**ft_split(char *str, char *charset)
{
	int		ary_len;
	char	**ary_of_str;
	char	**result;

	ary_len = get_ary_len(str, charset);
	ary_of_str = (char **)malloc(sizeof(char *) * (ary_len + 1));
	result = fill_ary(str, ary_of_str, charset);
	result[ary_len] = 0;
	return (result);
}

int main(void)
{
	char *x[1];
	int n = 0;
	char str[100000];
	char **seped_str;

	scanf("%c %d", x[0], &n);

	//全部ストリングで受け取る
	scanf("%s",str);
	//ft_split(str, x);
	seped_str = ft_split(str, x[0]); // x = 5, A1 = 555 のときに詰む

	//返ってきた二次配列に対してstrcat

	return (0);
}
