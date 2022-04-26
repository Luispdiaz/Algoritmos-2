def bienvenida():
    bienvenida = "Bienvenidos"
    bienvenida = bienvenida.center(50,"*")
    print(bienvenida)
def datos():
    while True:
        dato = input("Por favor, ingrese una palabra:")
        dato = dato.lower()
        if dato.isalpha():
                if "a" in dato:
                    dato = dato.replace("a","A") 
                if "e" in dato:
                    dato = dato.replace("e","E")
                if "i" in dato:
                    dato = dato.replace("i","I")
                if "o" in dato:
                    dato = dato.replace("o","O")
                if "u" in dato:
                    dato = dato.replace("u","U")    
                return dato
        else:
            print("El dato que ha ingresado no es valido")
            continue      
def main():
    bienvenida()
    dato = datos()
    print(dato)
main()