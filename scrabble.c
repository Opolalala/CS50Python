#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int alphabet[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int find_value(string word);

int main(void)
{
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");
    int sum1 = find_value(word1);
    int sum2 = find_value(word2);

    if (sum1 > sum2)
    {
        printf("Player 1 wins!\n");
    }
    else if (sum1 < sum2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int find_value(string word)
{
    int sum = 0;
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        if (isalpha(word[i]))
        {
            if (islower(word[i]))
            {
                word[i] = toupper(word[i]);
            }
            int ascii_value = word[i];
            int m = ascii_value - 65;
            sum += alphabet[m];
        }
    }
    return sum;
}