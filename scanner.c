/**
 * @file token.c
 * @author MJ Adendorff
 * @brief All about tokesn
 * @version 0.1
 * @date 2022-08-29
 * 
 */

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_ID_LENGTH 32
/* ASCII values */
#define CHAR_TAB 9
#define CHAR_LINE_BREAK 10
#define CHAR_RETURN 13

/* --- type definitions and constants --------------------------------------- */

/* Token enums for readability */
typedef enum {
    TOKEN_EOF,
    TOKEN_IDENTIFIER,
    TOKEN_PROPERTY,
    TOKEN_SETTING,
    TOKEN_OPEN_BRACKET,
    TOKEN_CLOSE_BRACKET,
    TOKEN_COLON,
    TOKEN_SEMICOLON,
} TokenType;

/* token data structure */
typedef struct {
	TokenType  type;
	union {
		char   lexeme[MAX_ID_LENGTH+1]; /* for identifiers */
		char  *string; /* for settings/properties */
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
void process_identifier(Token *token);
void init_scanner(FILE *in_file);

/* --- scanner interface ---------------------------------------------------- */

/* Initializes the scanner */
void init_scanner(FILE *in_file) {
    src_file = in_file;
    ln = 1;
    col = 0;
}

/* Moves to next character in  file */
void next_char() {
    ch = fgetc(src_file);
    col += 1;
    if (ch == CHAR_LINE_BREAK || ch == CHAR_RETURN) {
        ln += 1;
        col = 0;
    }
}

/* --- main ----------------------------------------------------------------- */

/* Testing the scanner */
int main() {
    return 0;
}

/* --- helper funcrtions ---------------------------------------------------- */

/* Get token string */
const char *get_token_string(TokenType type) {
	return token_names[type];
}