from enum import Enum

RESERVED_WORDS = ['int', 'char', 'if', 'else', 'for', 'while', 'return']

BIN_OPS = ['+', '-', '*', '/']

REL_OP = ['<', '>', '==', '!=', '<=', '>=', '=']

LOGIC_OP = ['&&', '||']

SEPARATORS = ['(', ')', '{', '}', '[', ']', ';', ',']

ALL_ELEMENTS = BIN_OPS + REL_OP + LOGIC_OP + SEPARATORS

TYPE_BY_OPERATORS = {
    '+': 'SUM',
    '-': 'SUB',
    '': 'MUL',
    '/': 'DIV',
    '<': 'LT',
    '>': 'GT',
    '==': 'EQ',
    '!=': 'NE',
    '<=': 'LE',
    '>=': 'GE',
    '=': 'ATTR',
    '&&': 'AND',
    '||': 'OR',
    '(': 'OPEN_BRACKET',
    ')': 'CLOSE_BRACKET',
    '{': 'OPEN_BRACE',
    '}': 'CLOSE_BRACE',
    '[': 'OPEN_SQUARE_BRACKET',
    ']': 'CLOSE_SQUARE_BRACKET',
    ';': 'SEMICOLON',
    ',': 'COMMA',
    'int': 'INT',
    'char': 'CHAR',
    'void': 'VOID',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'return': 'RETURN',
    '/*': 'OPEN_COMMENT',
    '*/': 'CLOSE_COMMENT',
}


class STATES(Enum):
    INITIAL = 0
    COMMENT = 1
    IDENTIFIER = 2
    LITERAL = 3
    NUMERIC = 4


