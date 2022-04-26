def bienvenida():
    bienvenida = "Bienvenido a su cuenta bancaria"
    bienvenida1 = bienvenida.center(50,"*")
    print(bienvenida1)
    print("Su saldo inicial es de 3480$")
def recaudacion_datos():
    while True:
        print("Ingrese 1 para retirar dinero \nIngrese 2 para depositar dinero")
        dato = input(">>")
        if dato.isalpha():
            print("El dato que ha ingresado no es valido")
            continue
        else:
            dato = int(dato)
        if dato == 1:
            return True
        elif dato == 2:
            return False
        else:
            print("El dato que ha ingresado no es valido")
            continue
def recaudacion_cantidad(booleano):
        if booleano == True:
            while True:
                cantidad = input("Ingrese la cantidad de dinero que desea retirar:")
                if cantidad.isnumeric():
                    cantidad = int(cantidad)
                    return cantidad
                else:
                    print("El dato que ha ingresado no es valido")
                    continue
        elif booleano == False:
            cantidad = int(input("Ingrese la cantidad de dinero que desea depositar:"))
            return cantidad
def operaciones(saldo, booleano, cantidad):
        if booleano == True:
            saldo -= cantidad
            if saldo < 0:
                print("La cantidad de dinero en la cuenta es insuficiente")
                saldo += cantidad
                return saldo
            return saldo
        elif booleano == False:
            saldo += cantidad
            return saldo
def impresion(cantidad, booleano, saldo):
    if booleano == True:
        if cantidad > saldo:
            print(f"Se han retirado 0$")
            print(f"Su saldo actual a la fecha (19/04/22) es de {saldo}$")
        else:
            print(f"Se han retirado {cantidad}$")
            print(f"Su saldo actual a la fecha (19/04/22) es de {saldo}$")
        print("Si desea depositar o retirar de nuevo presione '1', en su defecto presione '2'")
        date = input(">>")
        if date == "1":
            return True
        elif date == "2":
            print("Gracias, regrese pronto.")
            return False
        else: 
            print("El dato que ha ingresado no es valido")
    else:
        print(f"Se han depositado {cantidad}$")
        print(f"Su saldo actual a la fecha (19/04/22) es de {saldo}")
        print("Si desea depositar o retirar de nuevo presione '1', en su defecto presione '2'")
        date = input(">>")
        if date == "1":
            return True
        elif date == "2":
            print("Gracias, regrese pronto.")
            return False
        else: 
            print("El dato que ha ingresado no es valido")              
def main():
    bienvenida()
    saldo = 3480
    while True:
        booleano = recaudacion_datos()
        cantidad = recaudacion_cantidad(booleano)
        saldo = operaciones(saldo, booleano, cantidad)
        date = impresion(cantidad, booleano, saldo)
        if date == True:
            continue
        else:
            break       
main()