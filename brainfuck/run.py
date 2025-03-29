def brainfuck_interpreter(code):
    tape = [0] * 30000
    pointer = 0
    code_index = 0
    output = ""
    stack = []
    
    while code_index < len(code):
        command = code[code_index]
        
        if command == ">":
            pointer += 1
        elif command == "<":
            pointer -= 1
        elif command == "+":
            tape[pointer] = (tape[pointer] + 1) % 256
        elif command == "-":
            tape[pointer] = (tape[pointer] - 1) % 256
        elif command == ".":
            output += chr(tape[pointer])
        elif command == ",":
            tape[pointer] = ord(input("Input: ")[0]) % 256
        elif command == "[":
            if tape[pointer] == 0:
                while code[code_index] != "]" or stack:
                    code_index += 1
                    if code[code_index] == "[":
                        stack.append(code_index)
                    elif code[code_index] == "]" and stack:
                        stack.pop()
            else:
                stack.append(code_index)
        elif command == "]":
            if tape[pointer] != 0:
                code_index = stack[-1]
            else:
                stack.pop()
        
        code_index += 1
    
    return output

if __name__ == "__main__":
    # program = input("Enter Brainfuck code: ")
    # result = brainfuck_interpreter(program)
    # print("Output:", result)
    
    # this should print "Hello World!"
    input_code = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
    result = brainfuck_interpreter(input_code)
    print("Output:", result)
