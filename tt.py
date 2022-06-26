''' O número a ser calculado pode ser no mamximo 1000 a no mínimo -1000

Se um número já tiver sido calculado antes pela mesma pessoa vc não
calcula novamente mas lê o resultado do banco e retorna

Retorna tbm a data e hora de qdo a pessoa calculou aquele número pela primeira vez'''


# import re
#
# str = "paulo%$&"
# str1 = input("digita: ")
#
# regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
#
# if (regex.search(str1) == None):
#     print('Nao tem caracteres')
# else:
#     print('Tem caracteres')


# regex = ['@', '_', '!', '#', '$',
#                    '%', '^', '&', '*', '()',
#                    '<', '>', '?', '/\|', '}',
#                    '{', '~', ':']
#
# # regex = '[@_!#$%^&*()<>?/\|}{~:]'
#
#
# n = 'oi'
# for i in regex:
#     if i in n:
#         print('tem caractere')
#     else:
#         print('nao tem')

x = ["0"]
y = ''.join(x) # converting list into string
z = int(y)

print(type(x))
print(type(y))

a = int(y or 0)

print(type(a))