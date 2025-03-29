# Brainfuck Interpreter in Python

This is a simple Python implementation of a Brainfuck interpreter. Brainfuck is an esoteric programming language known for its minimalistic design and challenging syntax.

## About Brainfuck

It operates on an array of memory cells (tape) and uses a pointer to manipulate them. The language consists of only 8 commands, making it Turing complete yet extremely minimal.

### Commands
- `>` : Move the pointer to the right
- `<` : Move the pointer to the left
- `+` : Increment the value at the pointer (wraps at 256)
- `-` : Decrement the value at the pointer (wraps at 256)
- `.` : Output the value at the pointer as an ASCII character
- `,` : Accept one character input and store its ASCII value at the pointer
- `[` : Jump past matching `]` if the value at the pointer is 0
- `]` : Jump back to matching `[` if the value at the pointer is not 0

Any other characters are ignored by the interpreter.

### Memory
- The tape consists of 30,000 cells, each initialized to 0
- Each cell holds an 8-bit value (0-255)
- The pointer starts at cell 0

## Features of This Interpreter
- Clean, readable Python code
- Handles all standard Brainfuck commands
- Supports input via the comma (`,`) command
- Wraps values at 256 (8-bit simulation)
- Returns output as a string
