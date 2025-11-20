import random
from Validators import get_valid_name, get_valid_country, get_valid_height, get_valid_age, normalize_text, search_list
import uuid

print("Hola, mundo")
amigos=[]
dias=("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
alumnos=[]


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
    while True:
        try:
            entrada=input("Escribe un número y te doy el día siguiente. No ese. El siguiente. (0 para salir): ").strip()
            busqueda= int(entrada) if entrada else None
            if busqueda is None:
                print("Oye y si escribes algo...")
                continue
            elif busqueda==0:
                break
            elif 1<=busqueda<=7:
                print(f"Bueno. El día es: {dias[busqueda%7]}.")
                continue
            else:
                print("Opción inválida. Que sea del rango del 1 al 7.")
                continue
        except ValueError:
            print("Pero no es un número...")



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
                if fruta=="0":
                    break
                elif fruta in frutas:
                    frutas.remove(fruta)
                    print(f"Nos hemos despedido de {fruta}")
                    continue
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



def diccionario():

    while True:
        opcion=input("\nEstá en el apartado de diccionarios. ¿Qué operación desea realizar? (0 para salir)"
                    "\n1-. Crear alumno"
                    "\n2-. Lista de alumnos"
                    "\n3-. Editar alumno"
                    "\n4-. Borrar alumno"
                    "\n").strip()
        if opcion=="1":
            alumno={
                    "id": str(uuid.uuid4()),
                    "nombre":"",
                    "edad":None,
                    "altura":None,
                    "pais":"",
                    }

            print("\nCreemos tu usuario.")
            alumno["nombre"] = get_valid_name("Ingresa tu nombre: ")
            alumno["edad"] = get_valid_age("Ingresa tu edad: ")
            alumno["altura"] = get_valid_height("Ingresa tu altura (formato 1,75): ")
            alumno["pais"] = get_valid_country("Ingresa tu país: ")
            print("\n --- Datos del alumno ---")
            for clave, valor in alumno.items():
                print(f"{clave.capitalize():10}: {valor}")
            while True:
                confirmacion=input("\n¿Desea crear una entrada con los datos ingresados? (S/N): ").strip().lower()
                if confirmacion=="s":
                    alumnos.append(alumno)
                    print("\nAgregado exitosamente")
                    break
                elif confirmacion=="n":
                    break
                else:
                    print("\nOpción inválida. Intente de nuevo.")
                    continue

        elif opcion=="0":
            print("Saliendo del diccionario.")
            break
        
        elif opcion=="2":
            while True:
                opcion=input("\nSeleccione la búsqueda que desee realizar"
                            "\n1-. Lista completa"
                            "\n2-. Búsqueda por nombre"
                            "\n0-. Volver al menú"
                            "\n").strip()
                if opcion=="1":
                    print("--- Lista de alumnos ---")
                    for i, alumno in enumerate(alumnos, start=1):
                        print(f"{i:5}-. {alumno["nombre"]}")

                elif opcion=="2":
                    busqueda=input("Escriba el nombre del alumno que desea buscar (0 para salir): ").strip()
                    if busqueda=="0":
                        break
                    busqueda=normalize_text(busqueda)
                    alumnos_encontrados=[alumno for alumno in alumnos if busqueda in normalize_text(alumno["nombre"])]
                    if not alumnos_encontrados:
                        print("\nNo existe alumnos con este nombre.")
                        continue
                    elif len(alumnos_encontrados)>=1:
                        print(f"---Alumnos con el nombre '{busqueda.capitalize()}' encontrados---")
                        for i, alumno in enumerate(alumnos_encontrados, start=1):
                            print(f"{i}.- {alumno["nombre"]}")
                        try:
                            indice=int(input("Selecciona el número del alumno para ver sus datos: ").strip())-1
                            if  indice> len(alumnos_encontrados):
                                print("Seleccione un número válido.")
                                continue
                            else:
                                for clave, valor in alumnos_encontrados[indice].items():
                                    print(f"{clave.capitalize():5}: {valor}")
                                continue
                        except ValueError:
                            print("Selección inválida. Inténtalo de nuevo.")
                            continue

                elif opcion=="0":
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")
                    continue

        elif opcion=="3":
            while True:
                choice=input("Elija la operación a realizar:" 
                            "\n1-. Buscar por parámetro para editar"
                            "\n0-. Salir al menú"
                            "\n").strip()
                if choice=="0":
                    break
                elif choice=="1":
                    while True:
                        parametro=input("\nEscriba el parámetro para la búsqueda (0 para salir): ").strip()
                        if parametro=="0":
                            break
                        alumnos_encontrados=search_list(alumnos, parametro)
                        if not alumnos_encontrados:
                            print(f"No hay resultados con {parametro}.")
                            continue
                        elif len(alumnos_encontrados)>=1:
                            print(f"---Alumnos encontrados con el parámetro {parametro.capitalize()} encontrados---")
                            for i, alumno in enumerate(alumnos_encontrados, start=1):
                                print(f"{i}.- {alumno["nombre"]}")

                            try:
                                seleccion=int(input("Seleccione qué número de alumno quiere editar (0 para salir): ").strip())-1
                                if seleccion==-1:
                                    break
                                elif seleccion>len(alumnos_encontrados):
                                    print("Seleccione un número válido.")
                                    continue
                            except ValueError:
                                print("Ingrese un número válido.")
                                continue

                            alumno_obj=alumnos_encontrados[seleccion]

                            for clave, valor in alumno_obj.items():
                                print(f"{clave.capitalize():10}: {valor}")

                            cambio=input("\nSeleccione qué valor desea cambiar: ").strip().lower()

                            validadores={
                                "nombre": get_valid_name,
                                "edad": get_valid_age,
                                "altura": get_valid_height,
                                "pais":get_valid_country
                                }
                            
                            if cambio not in validadores:
                                print("Campo inválido.")
                                continue
                            nuevo_valor=validadores[cambio](f"Nuevo valor para {cambio}: ")
                            alumno_obj[cambio]=nuevo_valor
                            print("\nCampo actualizado correctamente.")
                        else:
                            print("Opción inválida. Intente de nuevo.")                        
                else:
                    print("Opción inválida. Intente de nuevo.")
                    continue
        
        elif opcion=="4":
            while True:
                choice=input("Elija una opción:" 
                            "\n1-. Buscar usuario para borrar."
                            "\n0-. Volver al menú"
                            "\n").strip()
                if choice=="0":
                    break
                elif choice=="1":
                        parametro=input("\nEscriba el parámetro para la búsqueda (0 para salir): ").strip()
                        if parametro=="0":
                            break
                        alumnos_encontrados=search_list(alumnos, parametro)
                        if not alumnos_encontrados:
                            print(f"No hay resultados con {parametro}.")
                            continue
                        elif len(alumnos_encontrados)>=1:
                            print(f"---Alumnos encontrados con el parámetro {parametro.capitalize()} encontrados---")
                            for i, alumno in enumerate(alumnos_encontrados, start=1):
                                print(f"{i}.- {alumno["nombre"]}")

                            try:
                                seleccion=int(input("Seleccione qué número de alumno quiere borrar (0 para salir): ").strip())-1
                                if seleccion==-1:
                                    break
                                elif seleccion>len(alumnos_encontrados):
                                    print("Seleccione un número válido.")
                                    continue
                            except ValueError:
                                print("Ingrese un número válido.")
                                continue
                            alumno_obj=alumnos_encontrados[seleccion]
                            while True:
                                confirm=input(f"¿Confirma que desea borrar al usuario {alumno_obj['nombre']} (S/N)?").strip().lower()
                                if confirm=="s":
                                    alumnos.remove(alumno_obj)
                                    print(f"Alumno {alumno_obj['nombre']} borrado correctamente.")
                                    break
                                elif confirm=="n":
                                    break
                                else:
                                    print("Selección inválida. Intente de nuevo.")
                                    continue
                else:
                    print("Opción inválida.")
                    continue
              

        else:
            print("Opción inválida. Intente de nuevo.")
            continue



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
            diccionario()
        elif opcion=="0":
            print("\nAdiós, crack.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
        
menu()