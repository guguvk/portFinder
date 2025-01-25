#!/usr/bin/python3

# portFinder v1.0, Author @guguvk (Axel González)

import socket, signal, threading
from pwn import *

signal.signal(signal.SIGINT, signal.SIG_DFL)

def main():
    try:
        target = input("Enter the target: ")
        ip = socket.gethostbyname(target)
        print(f"\nEscaneando {ip}\n")
        p1 = log.progress("")

        for i in range(1, 5536):
            with socket.socket() as s:
                p1.status(f"Probando con el puerto: {i}")
                response = s.connect_ex((ip, i))
                if response == 0:
                    print(f"Puerto abierto: {i}")
    except socket.gaierror:
        print("\nError: No se pudo resolver el nombre del host.")
    except ConnectionRefusedError:
        print("\nError: La conexión fue rechazada.")
    except TimeoutError:
        print("\nError: Se alcanzó el tiempo de espera.")
    except Exception as e:
        print(f"\nOcurrió un error: {e}")

threading.Thread(target=main).start()

