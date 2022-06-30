
animais = ['sapo', 'jacare', 'cobra']
numeros = [10, 20, 30]

zeros = [0]*4
uns = [1]*4
sequencia = [1, 2, 3]*3
entrada_do_usuario = ''

while entrada_do_usuario != 'saida':
    entrada_do_usuario = input('entrada do usuario: ')

    if entrada_do_usuario in animais:
        print(entrada_do_usuario, ' está na lista')
    else:
        print(entrada_do_usuario, ' não está na lista')