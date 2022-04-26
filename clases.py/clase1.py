#Tipos de datos, variables, operadores
#Variable: Espacio donde la computadora almacena un valor.
#Tipo de datos:
#Para diferenciar con que se trabaja, palabras, numeros, decimales, bool, etc.
#Para asignarle nombres a las variables se recomienda usar snake case: HOla_hola
#Operaciones basicas:
    #REcordar: Modulo % [EL resto de una division], Division entera // [Aunque de decimal, se toma el valor entero de la division],
#Ejenplos de tipos de datos:
#Entero
students = 25
#float
decimales = 4.5
#booleano
verdad = True
falso = False
#string
palabra = "Hola"

#Operadores logicos: Recordar != [distinto que], not [Negacion].
#Establecer variable con condicion
numero1 = 1
numero2 = 2
resultado = numero1 <= numero2
##print(resultado)
#Imprime un booleano, desmostrando que se cumple la condicion

#Ejemplos de strings: COncatenar
nombre = "Lebron"
apellido = "James"
##print(nombre + apellido)
#Lo imprime pegado

#Importante: EN vez de poner comillas dobles dentro de un string se coloca:
text = 'Welcome to \'UNIMET\'!'
text = 'Welcome to “UNIMET”!'

##print(ejemplo)
ejemplo1 = "Welcome to 'UNIMET'"

#strings en python
word_length = len("pneumonoultramicroscopicsilicovolcanoconiosis")
##print(word_length)
##print("Hola" * 3)


#Castear: Cambiar el tipo de dato
ejemplo = "1"
ejemplo = int(ejemplo)

def main():
    x = (((15 * 2 )/ 3 * 4 + ( 2 * 4 - 2) + 8 + (16 -10 * 2 )) * 2)
    print(x)
main()
