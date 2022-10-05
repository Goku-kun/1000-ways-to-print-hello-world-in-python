from sys import stdin


def eval(code):
  code = str(code)
  opcodes = [len(c.split()) for c in code.split('\n')]

  stack = []
  stack.append(stack)
  stack.append(stdin)
  stack.extend(opcodes)
  stack.append(0)

  load = False
  
  i = 2
  while i<=len(stack):
    opcode = stack[i]
    if opcode == 0: # exit
      if load:
        idx = stack[0].pop()
        value = stack[idx]
        stack.append(value)
      else:
        return stack[-1]
    elif opcode == 1: # chicken
      if load:
        idx = stack[1].pop()
        value = stack[idx]
        stack.append(value)
      else:
        stack.append("chicken")
    elif opcode == 2: # add
      a, b = stack.pop(), stack.pop()
      stack.append(b+a)
    elif opcode == 3: # subtract
      a, b = stack.pop(), stack.pop()
      stack.append(b-a)
    elif opcode == 4: # multiply
      a, b = stack.pop(), stack.pop()
      stack.append(a*b)
    elif opcode == 5: # compare
      a, b = stack.pop(), stack.pop()
      stack.append(a==b)
    elif opcode == 7: # store
      address, value = stack.pop(), stack.pop()
      stack[address] = value
    elif opcode == 8: # jump
      offset = stack.pop()
      if stack.pop():
        i += offset
    elif opcode == 9: # char
      char = stack.pop()
      stack.append(chr(char))
    elif opcode >= 10: # push
      stack.append(opcode-10)
    load = opcode == 6
    i += 1
  return stack[-1]

code = "chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken\nchicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken\n\nchicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken\n\nchicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken\nchicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken\n\nchicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken\n\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken\n\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken\nchicken chicken chicken chicken chicken chicken\n"
result = eval(code)

print(result)
