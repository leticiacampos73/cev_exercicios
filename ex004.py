o = input('digite algo:')
print(o, 'É do tipo primitivo', type(o))
print(o, 'Possui apenas números?', o.isnumeric(), '!')
print(o, 'Possui apenas letras?',  o.isalpha(), '!')
print(o, 'Possui letra ou número?', o.isalnum())
print(o, 'Possuia apenas letras maiúsculas?', o.isupper())
print(o, 'Possui apenas letras minúsculas?', o.islower())