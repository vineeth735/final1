#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_WORDS 1000
#define WORD_LEN 30

struct WordFreq {
    char word[WORD_LEN];
    int count;
};

void count_char_freq(const char *text);
void count_word_freq(const char *text);
void to_lower(char *str);
int find_word(struct WordFreq words[], int size, const char *word);
void sort_words(struct WordFreq words[], int size);

int main() {
    char text[10000];
    int choice;

    printf("=== Frequency Counter ===\n");
    printf("1. Enter text manually\n");
    printf("2. Read text from file\n");
    printf("Choose option (1/2): ");
    scanf("%d", &choice);
    getchar(); // Clear newline

    if (choice == 1) {
        printf("Enter text (end with `~` on a new line):\n");
        int i = 0;
        char ch;
        while ((ch = getchar()) != '~' && i < sizeof(text) - 1) {
            text[i++] = ch;
        }
        text[i] = '\0';
    } else if (choice == 2) {
        char filename[100];
        printf("Enter filename: ");
        scanf("%s", filename);
        FILE *f = fopen(filename, "r");
        if (!f) {
            printf("Cannot open file.\n");
            return 1;
        }
        fread(text, 1, sizeof(text), f);
        fclose(f);
    } else {
        printf("Invalid choice.\n");
        return 1;
    }

    count_char_freq(text);
    count_word_freq(text);

    return 0;
}

void count_char_freq(const char *text) {
    int freq[256] = {0};

    for (int i = 0; text[i] != '\0'; i++) {
        unsigned char c = text[i];
        freq[c]++;
    }

    printf("\n--- Character Frequency ---\n");
    for (int i = 0; i < 256; i++) {
        if (freq[i] > 0 && isprint(i)) {
            printf("'%c': %d\n", i, freq[i]);
        }
    }
}

void count_word_freq(const char *text) {
    struct WordFreq words[MAX_WORDS];
    int word_count = 0;

    char temp[10000];
    strcpy(temp, text);

    char *token = strtok(temp, " \t\n.,!?;:\"()[]{}<>");

    while (token != NULL) {
        to_lower(token);
        int index = find_word(words, word_count, token);
        if (index == -1 && word_count < MAX_WORDS) {
            strcpy(words[word_count].word, token);
            words[word_count].count = 1;
            word_count++;
        } else if (index != -1) {
            words[index].count++;
        }
        token = strtok(NULL, " \t\n.,!?;:\"()[]{}<>");
    }

    sort_words(words, word_count);

    printf("\n--- Word Frequency ---\n");
    for (int i = 0; i < word_count; i++) {
        printf("%s: %d\n", words[i].word, words[i].count);
    }
}

void to_lower(char *str) {
    for (int i = 0; str[i]; i++)
        str[i] = tolower(str[i]);
}

int find_word(struct WordFreq words[], int size, const char *word) {
    for (int i = 0; i < size; i++) {
        if (strcmp(words[i].word, word) == 0) {
            return i;
        }
    }
    return -1;
}

void sort_words(struct WordFreq words[], int size) {
    struct WordFreq temp;
    for (int i = 0; i < size - 1; i++) {
        for (int j = i + 1; j < size; j++) {
            if (words[j].count > words[i].count) {
                temp = words[i];
                words[i] = words[j];
                words[j] = temp;
            }
        }
    }
}

