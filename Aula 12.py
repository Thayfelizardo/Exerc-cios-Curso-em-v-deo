nome = str(input('Nome:'))
if nome == 'Thayná':
    print('Nome bonito')
elif nome == 'Tamara' or nome== 'Pedro' or nome== ' Judite':
    print('Nome normal')
elif nome in 'Ana Claudia Rosa Leticia ':
    print('Nome feminino')
else:
    print('Nome neutro')