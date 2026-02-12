def numero_palindromo(numero):
    numero_str = str(numero)
    return numero_str == numero_str[::-1]

assert numero_palindromo(121) == True
assert numero_palindromo(-121) == False
assert numero_palindromo(10) == False
assert numero_palindromo(-101) == False