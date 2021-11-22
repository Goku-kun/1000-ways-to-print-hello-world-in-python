"""print `Hello, World!` using brainfuck lang in python

Refs:
    - https://fatiherikli.github.io/brainfuck-visualizer/
    - https://en.wikipedia.org/wiki/Brainfuck
    - https://copy.sh/brainfuck/text.html
"""

def bf_eval(code):
    """Bruh"""

    output = ""
    mem = [0]
    mem_ptr = 0
    pc = 0 # program counter

    brackets_loop_stack = []

    while pc < len(code):

        if code[pc] == ">":
            mem_ptr += 1
            if pc >= len(mem):
                mem.append(0)

        elif code[pc] == "<":
            mem_ptr -= 1

        elif code[pc] == "+":
            mem[mem_ptr] += 1
            if mem[mem_ptr] > 255:
                mem[mem_ptr] = 0

        elif code[pc] == "-":
            mem[mem_ptr] -= 1
            if mem[mem_ptr] < 0:
                mem[mem_ptr] = 255

        elif code[pc] == '.':
            output += chr(mem[mem_ptr])
        
        elif code[pc] == ',':
            pass # idc

        elif code[pc] == '[':
            if mem[mem_ptr] != 0:
                brackets_loop_stack.append(pc)
            else:
                # run to the end of this bracket
                opened_bracket_count = 0
                while code[pc] != "]" or opened_bracket_count != 0:
                    if pc == len(code):
                        exit()
                    if code[pc] == "[":
                        opened_bracket_count += 1
                    if code[pc] == "]":
                        opened_bracket_count -= 1
                    pc += 1

        elif code[pc] == ']':
            
            if len(brackets_loop_stack) == 0:
                exit()
            if mem[mem_ptr] == 0:
                _ = brackets_loop_stack.pop()
            else:
                pc = brackets_loop_stack[-1]

        pc += 1

    return output

brainfuck_code = "-[------->+<]>-.-[->+++++<]>++.+++++++..+++.[->+++++<]>+.------------.---[->+++<]>.-[--->+<]>---.+++.------.--------.-[--->+<]>."
brainfuck_helloworld = bf_eval(brainfuck_code)

# assert "Hello, World" == brainfuck_helloworld

print(brainfuck_helloworld)
