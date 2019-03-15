import socket
import sys
IP = "10.108.33.19"
PORT = 8081

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.connect((IP, PORT))

def menu():
    print("Las operaciones de nuestra calculadora son:")
    print("0. Salir")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

try:
    menu()
    operacion = str(input("Indique la operación que desea realizar:"))
    operacion = int(operacion)
    if operacion != 0:
        numero_1 = str(input("Introduzca el número: "))
        numero_2 = str(input("Introduzca el siguiente número: "))
        operacion = str(operacion)
        mensaje = (operacion, numero_1, numero_2)
        mensaje = str(mensaje)
        mensaje=mensaje.replace("("," ").replace(")"," ")
        mensaje = ''.join(mensaje)
        serversocket.send(mensaje.encode())
        resultado = serversocket.recv(1024).decode()
        print("El resultado de la operación es: ", resultado)
    elif operacion ==0:
        sys.exit(1)

except socket.error:
    print("Ha habido un error con el socket")
except KeyboardInterrupt:
    print("Se ha interrumpido a conexión")
