n = int(input("Ingresar numero: ")) #Ingresar el valor a evaluar

lista =[]

while n != 1:          #Que esl ciclo funcione si los valores de n es diferente a 1
    if n % 2 == 0:     #Si el numero es par
        print("%d," %(n),end = "") #formato de cadenas con valor de n, imprima los valores en linea
        n = n / 2       #Como es par el valor lo divide en 2
    else:               #De lo contario 
        print("%d," %(n),end = "")  
        n = (n * 3) + 1     # Valor diferente multiplica por 3 y suma 1

    if n <= 1:
        print("1")

    for n in lista:
        f.write(n)
    f.close()