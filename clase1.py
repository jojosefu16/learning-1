import random

print("Hola, mundo")
amigos=[]
dias=("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

def parImpar():
    while True:
        numero=int(input("Introduzca un número para determinar si es positivo o negativo (0 para terminar): "))
        if numero==0:
            break
        elif numero <0 and numero%2 ==0:
            continue
        elif numero <0 and numero%2 !=0:
            print ("El número es negativo e impar.")
        elif numero >0 and numero%2 !=0:
            print ("El número es positvo e impar.")
        else:
            print ("El número es positivo y par.")



def adivina():
    print("Hola. Bienvenido a un simple juego. Adivinar el número del 1 al 10.")

    numero_secreto=random.randint(1,10)
    intentos=0

    while True:
        intento=int(input("Introduce tu número (0 para salir): "))
        intentos=intentos+1

        if (intento==numero_secreto):
            print(f"Correcto. El número era {numero_secreto}. Lo lograste en {intentos} intentos.")
            break
        elif (intento <numero_secreto and intento!=0):
            print("Es más alto...")
        elif (intento > numero_secreto and intento!=0):
            print("Es más bajo...")
        elif intento==0:
            break
        else:
            print("Introduce un número del 1 al 10.")



def listaAmigos(amigos):
    while True:  
        opcion=input("Seleccione la operación a realizar"
                "\n1-. Agregar amigos." 
                "\n2-. Ver lista de amigos."
                "\n0-. Volver al menú."
                "\n").strip()
        if opcion=="1":
            while True:
                nombre=input("Introduce el nombre de un amigo tuyo (0 para volver): ").strip().capitalize()
                if nombre=="0":
                    break
                else:
                    print(f"Se agregó a {nombre} a la lista.")
                    amigos.append(nombre)
        elif opcion=="2":
            print("\nTu lista de amigos:")
            for a in amigos:
                print(f" - {a}")         
            print(f"Tienes {len(amigos)} amigos registrados.")
            continue
        elif opcion=="0":
            return amigos
        else:
            print("Opción inválida. Inténtalo de nuevo.")



def tupla_practica(dias):
    print("No hay mucho que ver. Solo días de la semana. Obsérvalos.")
    for i, dia in enumerate(dias, start=1):
        print(f"Día: {i}- {dia}")



def sets_prueba():
    frutas=set()
    while True:
        opcion=input("Selecciona la operación a realizar con nuestro set de frutas." 
        "\n1-. Agregar frutas" 
        "\n2-. Modificar frutas"
        "\n3-. Eliminar frutas"
        "\n4-. Ver frutas"
        "\n0-. Salir"
        "\n").strip()
        if opcion=="1":
            while True:
             fruta=input("Escribe el nombre de la fruta antojada (0 para volver):").strip().capitalize()
             if fruta=="0":
                 break
             else:
                 frutas.add(fruta)
        elif opcion=="2":
            while True:
                fruta=input("Escribe el nombre de la fruta que quieres modificar (0 para salir): ").strip().capitalize()
                if fruta=="0":
                    break
                else:
                    if fruta in frutas:
                        reemplazo=input(f"Escribe la fruta para reemplazar a {fruta}: ").strip().capitalize()
                        frutas.remove(fruta)
                        frutas.add(reemplazo)
                    else:
                        print("Mi loco, dicha fruta no existe. Inténtalo de nuevo.")
        elif opcion=="3":
            while True:
                fruta=input("Escribe la fruta que quieres eliminar de la existencia (0 para salir): ").strip().capitalize()
                if fruta in frutas:
                    frutas.remove(fruta)
                    print(f"Nos hemos despedido de {fruta}")
                    continue
                elif fruta=="0":
                    break
                else:
                    print("No existe. De nuevo.")
        elif opcion=="4":
            print("\nLista de frutas:")
            for i in sorted(frutas):
                print(f"- {i}")
            print(f"\nTotal: {len(frutas)} frutas")
        elif opcion=="0":
            break
        else:
            print("Opción inválida.")



def menu():
    while True:
        opcion=input("\nBienvenido al menú para este programa random. Elige tu actividad random. (0 para salir)" 
        "\n1-. Par e impar.\n2-. Adivina adivinador."
        "\n3-. Lista de amigos"
        "\n4-. Tuplas?"
        "\n5-. Sets prueba"
        "\n6-. Agenda"
        "\nElige una opción: ").lower().strip()
        if opcion=="1":
            parImpar()
        elif opcion=="2":
            adivina()
        elif opcion=="3":
            listaAmigos(amigos)
        elif opcion=="4":
            tupla_practica(dias)
        elif opcion=="5":
            sets_prueba()
        elif opcion=="6":
            agenda()
        elif opcion=="0":
            print("\nAdiós, crack.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
        
menu()