def bienvenida():
    bienvenida = "Bienvenidos a la calculadora de numeros pares triangulares"
    bienvenida = bienvenida.center(50,"*")
    print(bienvenida)
    while True:
        numero = input("Ingrese un numero:")
        if numero.isnumeric:
            numero = int(numero)
            if numero >= 0:
                return numero
            else:
                print("El dato que ha ingresado no es valido")    
        else:
            print("El dato que ha ingresado no es valido")

def triangular(numero):
    aux = 1
    result = 0
    while result < numero:
        result = result + aux
        aux += 1
    if result == numero:
        return True
    else:
        return False

def par(numero):
    while numero > 0:
        numero -= 2
    if numero == 0:
        return True
    else:
        return False

def main():
    while True:   
        numero = bienvenida() 
        tri = triangular(numero)
        pares = par(numero)
        if tri == True and pares == True:
            print("El numero es par y triangular")
        elif tri == False and pares == True:
            print("El numero es par y no es triangular")
        elif tri == True and pares == False:
            print("El numero no es par y es triangular")
        else:
            print("EL numero no es par ni triangular")
        repeticion = input("Si quiere seguir usando la calculadora ingrese 1:")
        if repeticion == "1":
            continue
        else:
            break   
main()





