# Printing Hellow World using with statement 
with open('Target_file.txt', 'w') as file: 
    file.write('Hello, world !')   

with open('Target_file.txt', 'r') as file: 
    print(file.read())