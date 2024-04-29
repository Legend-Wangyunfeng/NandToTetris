
import re

IDENTIFIER_STR = "identifier"
KEYWORD_STR = "keyword"
SYMBOL_STR = "symbol"
INT_CONST_STR = "integerConstant"
STR_CONST_STR = "stringConstant"

REGEX_IDENTIFIER = re.compile("^\s*([a-zA-Z_][a-zA-Z1-9_]*)\s*")
REGEX_EMPTY_TEXT = re.compile("\s*")
REGEX_DIGIT = re.compile("^\s*(\d+)\s*")
REGEX_STRING = re.compile("^\s*\"(.*)\"\s*")
REGEX_KEYWORD = re.compile("^\s*(false|do|if|null|this|let|else|while|return|static|field|var|int|char|boolean|void|true|class|method|constructor|function)\s*")
REGEX_SYMBOL = re.compile("^\s*([{}()\[\].,;+\-*/&|~>=<])\s*")
REGEX_COMMENTS = "(//.*)|(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)"


KEYWORDS = [
    "CLASS",
    "DO", 
    "IF", 
    "ELSE", 
    "WHILE", 
    "RETURN", 
    "FUNCTION", 
    "CONSTRUCTOR", 
    "INT",
    "BOOLEAN", 
    "CHAR",
    "METHOD",
    "VOID", 
    "VAR", 
    "STATIC", 
    "FIELD", 
    "LET",
    "TRUE", 
    "FALSE",
    "NULL", 
    "THIS"
]

LEGAL_EXPRESSIONS = [
    "TRUE", 
    "FALSE",
    "NULL", 
    "THIS"
]

KEYWORD = "keyword"

SYMBOL = "symbol"

INT_CONST = "integerConstant"

STRING_CONST = "stringConstant"

IDENTIFIER = "identifier"

OPERATORS = [
    "+", 
    "/", 
    "-",
    "<", 
    ">", 
    "=", 
    "*", 
    "&", 
    "|",
    "^",
    "#"
]

OPERATORS_MAP = {
    "<": "&lt;",
    ">": "&gt;",
    "&": "&amp;",
    "\"": "&quot;"
}
COMMA = ","

EMPTY = ""

