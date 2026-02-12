def numero_palindromo(numero):
    # cria um texto baseado no numero
    numero_str = str(numero)
    # inverte o texto
    numero_invertido = numero_str[::-1]
    # compara o texto original com o texto invertido (o palindromo)
    return numero_str == numero_invertido

assert numero_palindromo(121) == True
assert numero_palindromo(-121) == False
assert numero_palindromo(10) == False
assert numero_palindromo(-101) == False