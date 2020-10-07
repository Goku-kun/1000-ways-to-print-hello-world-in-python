# Convert List into String

# Without using any Loop

# List of String elements
mylist = ['butter', 'jam', 'curd']
myStr = ','.join(mylist)
print (myStr)

# List of integer elements
mylist = [1, 11, 2222]
myStr = str(mylist).strip('[]')
print (myStr)

# Using Loop
mylist = [1, 22, 333]
myStr = ','.join(str(e) for e in mylist)
print (myStr)

# TASK: try removing the comma(s) from the string created
# from our original list
