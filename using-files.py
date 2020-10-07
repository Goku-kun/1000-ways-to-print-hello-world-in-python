#Printing Hello World using file operations

data_file = open("Target_file.txt","w")
data_file.write("Hello, World!")
data_file.close()

data_file = open("Target_file.txt","r")
print(data_file.read())