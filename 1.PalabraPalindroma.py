#Escribir procedimiento que ingresada una cadena informe si la misma es palíndroma
#Palindromo: Sinonimo de capicua: Se lee igual izquierda-derecha y viceversa.

#Declaracion variables
frase = input('Ingrese una palabra para saber si es palindroma')

#Declaracion procedimiento
def palindromo(frase=''):
    if frase==frase[::-1]:
        return 'La palabra es palindroma'
    else:
        return 'La palabra no es palindroma'

resultado = palindromo(frase)
print(resultado)

