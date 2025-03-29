import sys

def cow_interpreter(code):
    # Initialize memory tape: 30000 cells, all set to 0
    memory = [0] * 30000
    # Memory pointer starts at position 0
    pointer = 0
    # Current instruction index in the code
    code_index = 0
    # Output string to collect STDOUT
    output = ""
    # Stack for tracking MOO positions for loop control
    stack = []
    # Register for MMM instruction, initially None (no value)
    register = None
    
    # List of valid instructions for mOO execution, mapped to indices 0-11
    instruction_set = ["moo", "mOo", "moO", "mOO", "Moo", "MOo", "MoO", "MOO", "OOO", "MMM", "OOM", "oom"]

    # Main execution loop
    while code_index < len(code):
        # Current instruction to execute
        instruction = code[code_index]

        # Handle mOO: execute memory value as an instruction
        if instruction == "mOO":
            n = memory[pointer]
            # Check if n is invalid: <0, >11, or 3 (mOO itself, causing infinite loop)
            if n < 0 or n > 11 or n == 3:
                break  # Exit on invalid command
            instruction = instruction_set[n]  # Map memory value to instruction

        # moo: Jump back to matching MOO, searching in reverse and skipping previous instruction
        if instruction == "moo":
            if not stack:  # No matching MOO (stack empty)
                break  # Exit on unmatched moo
            # Pop the most recent MOO position
            code_index = stack.pop()
            continue  # Resume from matching MOO

        # mOo: Move pointer left
        elif instruction == "mOo":
            pointer -= 1
            if pointer < 0:  # Edge case: pointer underflow
                break  # Exit on out-of-bounds
            code_index += 1

        # moO: Move pointer right
        elif instruction == "moO":
            pointer += 1
            if pointer >= 30000:  # Edge case: pointer overflow
                break  # Exit on out-of-bounds
            code_index += 1

        # Moo: Input or output based on memory value
        elif instruction == "Moo":
            if memory[pointer] == 0:
                # Read single character from STDIN
                char = sys.stdin.read(1)
                memory[pointer] = ord(char) if char else 0  # 0 on EOF
            else:
                # Output ASCII character, modulo 256 to ensure valid range
                output += chr(memory[pointer] % 256)
            code_index += 1

        # MOo: Decrement memory value
        elif instruction == "MOo":
            memory[pointer] -= 1
            code_index += 1

        # MoO: Increment memory value
        elif instruction == "MoO":
            memory[pointer] += 1
            code_index += 1

        # MOO: Loop start, skip next instruction and jump to after matching moo if memory is 0
        elif instruction == "MOO":
            if memory[pointer] == 0:
                # Skip the next instruction
                if code_index + 1 >= len(code):
                    break  # No next instruction to skip, exit
                code_index += 2  # Move past skipped instruction
                nesting = 1  # Track nesting level
                # Search forward for matching moo
                while code_index < len(code) and nesting > 0:
                    if code[code_index] == "MOO":
                        nesting += 1
                    elif code[code_index] == "moo":
                        nesting -= 1
                    code_index += 1
                if nesting != 0:  # No matching moo found
                    break  # Exit on unmatched MOO
                # code_index is now after the matching moo
            else:
                # Non-zero: push position and continue
                stack.append(code_index)
                code_index += 1

        # OOO: Zero out current memory cell
        elif instruction == "OOO":
            memory[pointer] = 0
            code_index += 1

        # MMM: Copy to/from register
        elif instruction == "MMM":
            if register is None:
                register = memory[pointer]  # Copy memory to register
            else:
                memory[pointer] = register  # Paste register to memory
                register = None  # Clear register
            code_index += 1

        # OOM: Output memory value as integer
        elif instruction == "OOM":
            output += str(memory[pointer])
            code_index += 1

        # oom: Read integer from STDIN
        elif instruction == "oom":
            try:
                memory[pointer] = int(input())  # Read and convert to int
            except (ValueError, EOFError):
                memory[pointer] = 0  # Default to 0 on invalid input or EOF
            code_index += 1

        else:
            # Unrecognized instruction (safety check)
            code_index += 1

    return output

# Example usage (for testing):
if __name__ == "__main__":
    # Test code: "Hello" printer might need a specific COW program
    sample_code = f"""MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO
 MoO MoO Moo MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO Moo MoO MoO
 MoO MoO MoO MoO MoO Moo Moo MoO MoO MoO Moo OOO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO
 MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO Moo MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO
 MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO
 MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO
 MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO Moo MOo
 MOo MOo MOo MOo MOo MOo MOo MOo MOo MOo MOo MOo MOo MOo MOo MOo MOo MOo MOo MOo MOo MOo MOo MOo MOo MOo MOo MOo MOo MOo MOo MOo MOo MOo MOo
 MOo MOo MOo MOo MOo Moo MOo MOo MOo MOo MOo MOo MOo MOo Moo MoO MoO MoO Moo MOo MOo MOo MOo MOo MOo Moo MOo MOo MOo MOo MOo MOo MOo MOo Moo
 OOO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO Moo"""
    sample_code = [
        i.strip() for i in sample_code.split()
    ]
    
    res = cow_interpreter(sample_code)
    print(f"Output: {res}")
    # Expected output: "Hello, world!"