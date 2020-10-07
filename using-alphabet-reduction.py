import string
def generateAlphabet():
    return string.ascii_lowercase + string.ascii_uppercase

def reduceTo(reducable, character):
    newString = "";
    for i in range(0,len(reducable)):
        if reducable[i] == character:
            newString += character
    return newString

HelloWorld = ""
HelloWorld += reduceTo(generateAlphabet(),'H')
HelloWorld += reduceTo(generateAlphabet(), 'e');
HelloWorld += reduceTo(generateAlphabet(), 'l');
HelloWorld += reduceTo(generateAlphabet(), 'l');
HelloWorld += reduceTo(generateAlphabet(), 'o');
HelloWorld += ", ";
HelloWorld += reduceTo(generateAlphabet(), 'W');
HelloWorld += reduceTo(generateAlphabet(), 'o');
HelloWorld += reduceTo(generateAlphabet(), 'r');
HelloWorld += reduceTo(generateAlphabet(), 'l');
HelloWorld += reduceTo(generateAlphabet(), 'd');
HelloWorld += "!";
print(HelloWorld)
    
