# Whatalang

A programming language built around a single global state with reactive updates.

## Features
- Single global state management
- Reactive programming
- Functional operations
- Simple, readable syntax

## Development Status
🚧 In Development - Basic parser and state management

## Getting Started
```bash
pip install -r requirements.txt
python -m pytest tests/
```

## Syntax Examples
```wa
state {
  counter: 0,
  user: { name: "John", age: 30 }
}

set counter = 1
print state
```

## Project Structure
```
src/
├── parser/     # Language parser and lexer
├── state/      # State management system
└── grammar.py  # Language grammar definition

tests/          # Test suite
```
