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

# db = [{'a': 1}, {'b': 2}, {'c': 1}]
#
# result_list = [int(v) for lst in db for k, v in lst.items()]
# print(result_list)


# for i, v in db.items():
#     list_value.append(v)
#
# print(list_value)

# result_list = []
# for d in db:
#     list_value.append([int(v) for k,v in d.items()])
#
# print(result_list)

a = ['paulo', 'alan', 'joao']
b = 'paulo'

v = [1, 2, 3]
f = 4

if b in a and f in v:
    print(b, 'e', f, ' esta na lista')
else:
    print(b, 'e', f, 'nao esta na lista')

'''
result_list = []
for d in qs:
    result_list.append([int(v) for k,v in d.items()])
'''