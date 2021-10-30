import webbrowser
import os

f = open("helloworld.html", "w")
f.write("""<html>
        <head> <title>Hello world !</title> </head>
        <body><p>Hello world !</p></body>
        </html>""")

f.close()

webbrowser.open('file://' + os.path.realpath("helloworld.html"))



