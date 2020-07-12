import os
from markdown2 import markdown

dir = os.getcwd()
file = open(dir + "/in/test.md", 'r')
input = file.read()
file.close()

html = markdown(input, extras=['fenced-code-blocks'])

file = open(dir + "/out/test.html", 'w')
file.write(html)
file.close()
