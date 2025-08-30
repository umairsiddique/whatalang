"""
Whatalang Grammar Definition
"""

# Basic token types
TOKENS = {
    'KEYWORD': ['state', 'set', 'print', 'react', 'to', 'when', 'default'],
    'OPERATOR': ['=', '+', '-', '*', '/', '==', '!=', '>', '<', '>=', '<='],
    'DELIMITER': ['{', '}', '[', ']', ':', ',', '(', ')'],
    'LITERAL': ['STRING', 'NUMBER', 'BOOLEAN', 'NULL'],
    'IDENTIFIER': 'IDENTIFIER'
}

# Basic grammar rules (simplified for now)
GRAMMAR_RULES = {
    'program': 'statement*',
    'statement': 'state_decl | set_statement | print_statement',
    'state_decl': 'state { key_value_pair* }',
    'key_value_pair': 'identifier : value',
    'value': 'literal | object | array',
    'object': '{ key_value_pair* }',
    'array': '[ value* ]',
    'set_statement': 'set path = expression',
    'print_statement': 'print expression',
    'path': 'identifier ( . identifier | [ expression ] )*',
    'expression': 'literal | identifier | path'
}
