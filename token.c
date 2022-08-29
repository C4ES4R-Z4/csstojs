/**
 * @file token.c
 * @author MJ Adendorff
 * @brief Tokens
 * @version 0.1
 * @date 2022-08-29
 * 
 * @copyright Copyright (c) 2022
 * 
 */

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#define MAX_ID_LENGTH 32

/* --- type definitions and constants --------------------------------------- */

typedef enum {
    TOKEN_EOF,
    /* Identifier tokens */
    TOKEN_IDENTIFIER,
    /* targeted property tokens */
    TOKEN_PROPERTY,
    TOKEN_SETTING,
    /* other tokens */
    TOKEN_OPEN_BRACKET,
    TOKEN_CLOSE_BRACKET,
    TOKEN_COLON,
    TOKEN_SEMICOLON,
} TokenType;

typedef struct {
	TokenType  type;
	union {
		char   lexeme[MAX_ID_LENGTH+1];
		char  *string;
	};
} Token;

/* --- global static variables ---------------------------------------------- */

static FILE *src_file;
static char ch;
static int col;
static int ln;

static char *token_names[] = {
	"end-of-file","identifier", "css property", "css setting",
	"'{'", "'}'", "':'", "';'"
};

/* --- function prototypes -------------------------------------------------- */

const char *get_token_string(TokenType type);
static void process_identifier(Token *token);

/* --- scanner interface ---------------------------------------------------- */


/* --- main ----------------------------------------------------------------- */

int main() {
    printf("%s\n", get_token_string(TOKEN_PROPERTY));
    return 0;
}

/* --- helper funcrtions ---------------------------------------------------- */

const char *get_token_string(TokenType type)
{
	assert(type >= 0 && type < (sizeof(token_names)/sizeof(char *)));
	return token_names[type];
}