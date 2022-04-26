#Una palabra o número palíndromo son aquellos que se leen igual de izquierda a derecha. Por ejemplo: 101 es un número palíndromo, 
# y 236 no lo es. Ana es una palabra palíndroma y pan no lo es.
#Diseña un programa que determine si un número o palabra ingresados por teclado, son palíndromos o no.

def bienvenida():
    bienvenida = "Bienvenido a la calculadora de Palindromos"
    bienvenida = bienvenida.center(50,"*")
    print(bienvenida)
    print("Una palabra o número palíndromo son aquellos que se leen igual de izquierda a derecha.")
def dato():
    dato = input("Ingrese un numero o una palabra:")
    while True:
        if dato.isalpha() or dato.isnumeric():
            return dato
        else:
            print("El dato que ha ingresado no es valido")
            continue
def calculadora(dato1):
    if dato1 == dato1[::-1]:
        print(f"{dato1} es palindromo")
    else:
        print(f"{dato1} no es palindromo")
def main():
    bienvenida()
    while True:
        dato1 = dato()
        calculadora(dato1)
        salida = input("Si quiere continuar ingrese '1':")
        if salida == "1":
            continue
        else:
            print("Gracias por utilizar la calculadora de palindromos.")
            break
main()
