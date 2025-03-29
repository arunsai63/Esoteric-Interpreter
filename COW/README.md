# COW Interpreter in Python

This is a Python implementation of an interpreter for the COW programming language, an esoteric Brainfuck variant designed with a bovine theme. COW uses twelve "moo"-based instructions to manipulate memory and produce output.

## About COW

COW is a Turing-complete esoteric language inspired by Brainfuck but with a humorous twist—all commands are variations of "moo" (e.g., `moO`, `MoO`, `MOO`). It was designed to playfully explore minimalism and creativity in programming, featuring a register alongside the traditional tape and pointer.

### Commands
- `MoO` : Move pointer right
- `mOo` : Move pointer left
- `moO` : Increment value at pointer
- `mOO` : Decrement value at pointer
- `Moo` : If value is 0, input a character; else, output value as a character
- `MOO` : Jump to matching `moo` if value is not 0 (loop end)
- `moo` : Jump past matching `MOO` if value is 0 (loop start)
- `OOO` : Set value at pointer to 1
- `MMM` : Copy register value to pointer
- `mOo` : Copy value at pointer to register
- `MOo` : Set value at pointer to 0
- `OOM` : Output value at pointer as a character

All other character combinations are ignored.

### Memory
- Tape of 30,000 cells, initialized to 0
- Each cell holds an integer value
- Pointer starts at cell 0
- Single register for temporary storage

## Features of This Interpreter
- Simple, readable Python code
- Stack-based loop handling for `moo` and `MOO`
- Supports all 12 COW commands
- Handles input/output via `Moo` and `OOM`
- Returns output as a string
