l=[1, 0, 2, 0, 'hello', ' ', []]
print(list(filter(bool, l)))

l=list('HELLO')
p=l[0], l[-1], l[1:3]
print('{a}{b}{a}'.format(a='hello', b='world'))

D=dict(p='san', q='foundry')
print( '{p}-{q}'.format(**D))