import re

str = "paulo%$&"
str1 = input("digita: ")

regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

if (regex.search(str1) == None):
    print('Nao tem caracteres')
else:
    print('Tem caracteres')