import socket
import sys 

IP = "10.108.33.19"
PORT = 8081

def suma(a, b):
    operacion = a+b
    return str(operacion)

def resta(a,b):
    operacion = a-b
    return str(operacion)

def multiplicacion(a,b):
    operacion = a*b
    return str(operacion)

def division(a,b):
    if b == 0:
        return 0
    else:
        operacion = a/b
        return str(operacion)

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname=IP

try:
    serversocket.bind((hostname, PORT))
    serversocket.listen(5)

    condicion = True
    while condicion:
        print("Esperando conexiones:") 
        (clientsocket, address) = serversocket.accept()
        mensaje = clientsocket.recv(1024).decode()
        print(mensaje)
        mensaje=mensaje.replace(" ","").replace("'","")
        mensaje=mensaje.split(",")
        print(mensaje)
        print(mensaje[0])

        op = int(mensaje[0])
        a = int(mensaje[1])
        b = int(mensaje[2])
        op = int(op)
        a = int(a)
        b = int(b)
        resultado = 0
        
        if op == 1:
            resultado = suma(a, b)
            clientsocket.send(resultado.encode())

        elif op == 2:
            resultado = resta(a,b)
            clientsocket.send(resultado.encode())

        elif op == 3:
            resultado = multiplicacion(a,b)
            clientsocket.send(resultado.encode())

        elif op == 4:
            resultado = division(a,b)
            clientsocket.send(resultado.encode())

        else:
            print("Esa operación no está permitida")

except socket.error:
    print("Error en el socket")
except ValueError:
    print("Esa operación no se puede realizar")
except IndexError:
    print(" ")
except KeyboardInterrupt:
    print("La conexión ha sido interrumpida")

