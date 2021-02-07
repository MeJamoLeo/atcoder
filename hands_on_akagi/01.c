#include <stdio.h>

int main(void)
{
  char a;
  char b;
  char c;
  // printf("文字を入力してください\n");

  scanf("%c%c%c", &a, &b, &c);

  if (a == b && b == c) {
    printf("Won\n");
  }
  else {
    printf("Lost\n");
  }
}
