from tabulate import tabulate
from typing import List, Tuple

######################################################
###################### OPCIONES ######################
######################################################

def imprimir_opciones(menu: dict) -> None:
    """
    Imprime las opciones del menú en formato tabular.
    Pre-condicion: El diccionario 'menu' debe contener al menos una entrada.
    Post-condicion: Imprime las opciones del menú.

    Parametros:
    - menu (dict): Un diccionario que representa las opciones del menú.
    """
    print(tabulate(menu.items(), tablefmt="presto"))

def opciones() -> None:
    """
    Muestra las opciones principales del programa.
    Pre-condicion: -
    Post-condicion: Llama a la función imprimir_opciones para mostrar las opciones del menú principal.
    """
    menu = {
        0: 'Salir.',
        1: 'Cargar datos.',
        2: 'Mostrar datos.',
        3: 'Tres motos más caras por marca.',
        4: 'Agregar datos.',
        5: 'Exportar motos por marca.',
        6: 'Comprar moto.'
    }
    imprimir_opciones(menu)

def sub_opciones() -> None:
    """
    Muestra las subopciones para el menú de mostrar datos.
    Pre-condicion: -
    Post-condicion: Llama a la función imprimir_opciones para mostrar las subopciones.
    """
    menu = {
        1: 'Mostrar motos',
        2: 'Mostrar motos baratas',
        3: 'Mostrar motos caras'
    }
    imprimir_opciones(menu)

###########################################################################
###################### OBTENER DATOS / CREAR ARCHIVO ######################
###########################################################################

def cargar_datos(archivo: str, separador: str) -> Tuple[List[List[str]], List[str]]:
    """
    Carga datos desde un archivo y devuelve una tupla con la lista de datos y el encabezado.
    Pre-condicion: El archivo proporcionado debe existir en la ruta especificada.
    Post-condicion: Retorna una tupla donde el primer elemento es una lista de listas representando los datos y el segundo elemento es una lista representando el encabezado.

    Parametros:
    - archivo (str): La ruta al archivo que contiene los datos.
    - separador (str): El caracter utilizado para separar los elementos en cada línea.

    Retorna:
    Tuple[List[List[str]], List[str]]: Una tupla con la lista de datos y el encabezado.
    """
    datos = []
    encabezado = []
    try:
        # Lee el archivo y obtiene los datos
        with open(archivo, "rt", encoding="utf-8") as arch:
            encabezado = arch.readline().strip().split(separador)
            datos = list(linea.strip().split(separador) for linea in arch)
    except FileNotFoundError:
        print("El archivo no existe, intentelo mas tarde")
    except Exception as e:
        print(f"Error: {e}")
    else:
        print("Datos cargados exitosamente.")
    return datos, encabezado

###########################################################
###################### AGREGAR MOTOS ######################
###########################################################

def pedir_marca(marcas:list[str]) -> str:
    """
    Solicita al usuario que ingrese una marca de moto válida y la devuelve.
    Pre-condicion: La lista de marcas no debe estar vacía.
    Post-condicion: Retorna la marca de moto ingresada por el usuario, que debe estar presente en la lista de marcas.

    Parametros:
    - marcas (List[str]): Lista de marcas de moto disponibles.

    Retorna:
    str: La marca de moto ingresada por el usuario.
    """
    while True:
        print(tabulate([marcas], tablefmt="grid"))
        marca = input("Ingrese una de las marcas mostradas: ")
        if marca.lower() in marcas:
            return marca.lower()
        else:
            print("Dato inválido. Ingrese una marca válida.")

def pedir_modelo(datos: List[List[str]], marca: str) -> str:
    """
    Solicita al usuario que ingrese el modelo de una moto válida para una marca específica y lo devuelve.
    Pre-condicion: La lista de datos no debe estar vacía.
    La marca proporcionada debe estar presente en al menos una entrada de la lista de datos.
    Post-condicion: Retorna el modelo de moto ingresado por el usuario, que debe estar presente en la lista de modelos correspondientes a la marca dada.
    Parametros:
    - datos (List[List[str]]): Lista de datos de motos.
    - marca (str): La marca de moto para la cual se solicita el modelo.

    Retorna:
    str: El modelo de moto ingresado por el usuario.
    """
    modelos = list(modelo[1] for modelo in datos if modelo[0] == marca)
    while True:
        print(tabulate([modelos], tablefmt="grid"))
        data = input("Ingrese el modelo de la moto: ")
        if data.lower() in modelos:
           return data.lower()
        else:
            print("Dato inválido. Ingrese un modelo válido.")

def pedir_anio() -> str:
    """
    Solicita al usuario que ingrese el año de fabricación de una moto válida y lo devuelve.
    Pre-condicion: -
    Post-condicion: Retorna el año de fabricación de la moto ingresado por el usuario, que debe ser un valor numérico entre 1950 y 2050.
    Retorna:
    str: El año de fabricación de la moto ingresado por el usuario.
    """
    while True:
        anio = input("Ingrese el anio de la moto: ")
        if anio.isdigit() and int(anio) >= 1950 and int(anio) <= 2050:
            return anio
        else:
            print("Dato inválido. Ingrese un anio válido.")
        
def pedir_precio() -> str:
    """
    Solicita al usuario que ingrese el precio de una moto y lo devuelve.
    Pre-condicion: -
    Post-condicion: Retorna el precio de la moto ingresado por el usuario, que debe ser un valor numérico mayor que 0.
    Retorna:
    str: El precio de la moto ingresado por el usuario.
    """
    while True:
        precio = input("Ingrese el precio de la moto: ")
        if precio.isdigit() and int(precio) > 0:
            return precio
        else:
            print("Dato inválido. Ingrese un precio válido.")

def agregar_datos(datos: List[List[str]]) -> None:
    """
    Agrega nuevos datos de motos al archivo existente.
    Pre-condicion: -
    Post-condicion: Agrega las nuevas entradas de datos al archivo

    Parametros:
    - datos (List[List[str]]): Lista de listas representando los datos de las motos.
    """
    try:
        with open(archivo, "at", encoding="utf-8") as arch:
            for linea in datos:
                arch.write(separador.join(linea) + "\n")
    except Exception as e:
        print(f"Error: {e}")

def agregar_motos(datos: List[List[str]], marcas: List[str]) -> List[List[str]]:
    """
    Permite al usuario agregar nuevas motos y las devuelve como una lista.
    Pre-condicion: La lista de marcas no debe estar vacía.
    Post-condicion: Retorna una lista de listas que representan los datos de las nuevas motos ingresadas por el usuario

    Parametros:
    - datos (List[List[str]]): Lista de listas representando los datos de las motos existentes.
    - marcas (List[str]): Lista de marcas de moto disponibles.

    Retorna:
    List[List[str]]: Lista de listas representando los datos de las nuevas motos.
    """
    nuevas_motos = []
    while True:
        marca = pedir_marca(marcas)
        modelo = pedir_modelo(datos, marca)
        precio = pedir_precio()
        anio = pedir_anio()
        nuevas_motos.append([marca, modelo, precio, anio])
        
        confirm = input("Desea agregar otra moto? (s/n): ")
        if confirm == "n":
            break
    return nuevas_motos

###########################################################
###################### MOSTRAR DATOS ######################
###########################################################

def mostrar_motos_totales(datos: List[List[str]], encabezado: List[str]) -> None:
    """
    Muestra todas las motos existentes.
    Pre-condicion:-
    Post-condicion: Muestra todas las motos existentes en formato tabular.

    Parametros:
    - datos (List[List[str]]): Lista de listas representando los datos de las motos.
    - encabezado (List[str]): Lista de encabezados de columna.
    """
    print(tabulate(datos, encabezado, tablefmt="github"))

def validar_precio() -> int:
    """
    Solicita al usuario que ingrese un precio válido y lo devuelve como un entero.
    Pre-condicion:-
    Post-condicion: Retorna el precio ingresado por el usuario, que debe ser un valor numérico mayor que 0.

    Retorna:
    int: El precio ingresado por el usuario.
    """
    while True:
        data = input('ingrese un precio: $')
        if data.isdigit() and int(data) > 0:
            return int(data)  
        else:
            print("Dato invalido.")
    
def mostrar_moto_mas_cara(datos: List[List[str]], encabezado: List[str]) -> None:
    """
    Muestra las motos cuyo precio es igual o superior al ingresado por el usuario.
    Pre-condicion:-
    Post-condicion: Muestra las motos cuyo precio es igual o superior al valor ingresado por el usuario, en formato tabular.

    Parametros:
    - datos (List[List[str]]): Lista de listas representando los datos de las motos.
    - encabezado (List[str]): Lista de encabezados de columna.
    """
    precio = validar_precio()
    mas_cara = list(lista for lista in datos if int(lista[2]) >= precio)
    print(tabulate(mas_cara, encabezado, tablefmt="github"))
    
def mostrar_moto_mas_barata(datos: List[List[str]], encabezado: List[str]) -> None:
    """
    Muestra las motos cuyo precio es igual o inferior al ingresado por el usuario.
    Pre-condicion:-
    Post-condicion: Muestra las motos cuyo precio es igual o inferior al valor ingresado por el usuario, en formato tabular.

    Parametros:
    - datos (List[List[str]]): Lista de listas representando los datos de las motos.
    - encabezado (List[str]): Lista de encabezados de columna.
    """
    precio = validar_precio()
    mas_barata = list(lista for lista in datos if int(lista[2]) <= precio)
    print(tabulate(mas_barata, encabezado, tablefmt="github"))

def mostrar_datos(datos: List[List[str]], encabezado: List[str]) -> None:
    """
    Permite al usuario elegir entre mostrar todas las motos, las más caras o las más baratas, y muestra los resultados.
    Pre-condicion:-
    Post-condicion: Muestra todas las motos, las más caras o las más baratas según la opción seleccionada por el usuario, en formato tabular.
    Parametros:
    - datos (List[List[str]]): Lista de listas representando los datos de las motos.
    - encabezado (List[str]): Lista de encabezados de columna.
    """
    opcion = input("Ingrese una de las opciones: ")
    if opcion == "1":
        mostrar_motos_totales(datos, encabezado)
    elif opcion == "2":
        mostrar_moto_mas_cara(datos, encabezado)
    elif opcion == "3":
        mostrar_moto_mas_barata(datos, encabezado)
    else:
        print("Opcion fuera de rango.")

###############################################################
###################### 3 motos mas caras ######################
###############################################################

def obtener_tres_motos_mas_caras_por_marca(datos: List[List[str]]) -> None:
    """
    Muestra las tres motos más caras por marca.
    Pre-condicion:-
    Post-condicion: Muestra las tres motos más caras por marca en formato tabular.

    Parametros:
    - datos (List[List[str]]): Lista de listas representando los datos de las motos.
    """
    motos_por_marca = {}

    for moto in datos:
        marca = moto[0]
        modelo = moto[1]
        valor = int(moto[3])

        if marca not in motos_por_marca:
            motos_por_marca[marca] = [(modelo, valor)]
        else:
            motos_por_marca[marca].append((modelo, valor))

    # Ordenar las motos de cada marca por valor de forma descendente
    for marca, motos in motos_por_marca.items():
        motos_por_marca[marca] = sorted(motos, key=lambda x: x[1], reverse=True)[:3]

        
    print("Las tres motos más caras por marca:")
    for marca, motos in motos_por_marca.items():
        print(f"\nMarca: {marca}")
        print(tabulate(motos, headers=['Modelos', 'Precio'], tablefmt="pretty"))

############################################################
###################### EXPORTAR MARCA ######################
############################################################

def validar_marca(marcas: List[str]) -> str:
    """
    Solicita al usuario que ingrese una marca válida y la devuelve.
    Pre-condicion: La lista de marcas no debe estar vacía.
    Post-condicion: Retorna la marca de moto ingresada por el usuario, que debe estar presente en la lista de marcas.

    Parametros:
    - marcas (List[str]): Lista de marcas de moto disponibles.

    Retorna:
    str: La marca ingresada por el usuario.
    """
    while True:
        opcion = input('Ingrese la marca (honda, yamaha, suzuki, ktm, kawasaki): ')
        if opcion.lower() in marcas:
            return opcion.lower()
        else:
            print('Error, ingrese una marca válida')

def motos_x_marca(datos: List[List[str]], marca: str) -> List[List[str]]:
    """
    Filtra las motos por marca y devuelve una lista con los datos correspondientes.
    Pre-condicion:-
    Post-condicion: Retorna una lista de listas que representan los datos de las motos filtradas por la marca especificada.


    Parametros:
    - datos (List[List[str]]): Lista de listas representando los datos de las motos.
    - marca (str): La marca por la cual se filtran las motos.

    Retorna:
    List[List[str]]: Lista de listas representando los datos de las motos de la marca especificada.
    """
    return [moto for moto in datos if moto[0] == marca]

def exportar_datos(marca: str, separador: str, exportar: List[List[str]], encabezado: List[str]) -> None:
    """
    Exporta los datos de las motos de una marca a un archivo CSV.
    Pre-condicion:-
    Post-condicion: Exporta los datos de las motos de la marca especificada a un archivo CSV con el nombre de la marca.

    Parametros:
    - marca (str): La marca de las motos a exportar.
    - separador (str): El separador a utilizar en el archivo CSV.
    - exportar (List[List[str]]): Lista de listas representando los datos de las motos a exportar.
    - encabezado (List[str]): Lista de encabezados de columna.
    """
    try:
        with open(f"{marca}.csv", "wt", encoding="utf-8") as arch:
            arch.write(separador.join(encabezado) + "\n")
            for linea in exportar:
                arch.write(separador.join(linea) + "\n")
    except Exception as e:
        print(f"Error: {e}")

#####################################################
###################### CARRITO ######################
#####################################################

def carrito_motos(datos: list[list[str]], encabezado:list[str])-> tuple[list[list[str]], list[list[str]]]:
    """
    Permite al usuario crear un carrito de compras con motos y devuelve los datos actualizados y el carrito.
    Pre-condicion: -
    Post-condicion: Retorna una tupla con los datos de las motos actualizados después de la compra y el carrito de motos.

    Parametros:
    - datos (List[List[str]]): Lista de listas representando los datos de las motos disponibles.
    - encabezado (List[str]): Lista de encabezados de columna.

    Retorna:
    Tuple[list[list[str]], list[list[str]]]: Tupla con los datos actualizados y el carrito de motos.
    """
    carrito = []
    stock = []
    while True:
        print(tabulate(datos, encabezado, tablefmt="github", showindex="always"))
        indice_moto = input("Ingrese el indice de la moto a comprar (f para finalizar): ")
        if indice_moto == 'f':
            print("Carrito:\n",tabulate(carrito, encabezado, tablefmt="github"))
            print(f"Total: ${sum(int(precio[2]) for precio in carrito)}")
            confirmacion = input('Desea confirmar la compra (S/N): ').lower()
            if confirmacion == 's':
                for elemento in carrito:
                    datos.remove(elemento)
                return datos, carrito
            elif confirmacion == 'n':
                return datos, []
            else:
                print("Opcion invalida.")
        elif indice_moto.isdigit() and int(indice_moto) >= 0 and int(indice_moto) <= (len(datos) -1):
            stock.append(indice_moto)
            if indice_moto not in stock:
                carrito.append(datos[int(indice_moto)])
            else:
                print("Ya selecciono esta moto.")
        else:
            print("Caracter invalido.")

def actualizar_datos(archivo: str, separador: str, encabezado: list[str], datos: list[list[str]]) -> None:
    """
    Actualiza el archivo de datos con los nuevos datos de motos.
    Pre-condicion:  -
    Post-condicion: Actualiza el archivo de datos con los nuevos datos de motos proporcionados.

    Parametros:
    - archivo (str): Ruta del archivo de datos a actualizar.
    - separador (str): El separador a utilizar en el archivo.
    - encabezado (List[str]): Lista de encabezados de columna.
    - datos (List[List[str]]): Lista de listas representando los datos de las motos.
    """
    try:
        with open(archivo, "wt", encoding="utf-8") as arch:
            arch.write(separador.join(encabezado) + "\n")
            for linea in datos:
                arch.write(separador.join(linea) + "\n")
    except Exception as e:
        print(f"Error: {e}")

##################################################
###################### MENU ######################
##################################################

def menu()-> None:
    """
    Función principal que maneja las opciones del programa de gestión de motos.

    """
    datos = []
    while True:
        opciones()
        data = input("Ingrese una de las opcines (0 para salir): ")
        if not data.isdigit():
            print("Caracter invalido.")
        elif data == "0":
            print("Finalizando Programa...")
            return
        elif data == "1":
            datos, encabezado = cargar_datos(archivo, separador)
            marcas = sorted(set(elem[0].lower() for elem in datos))
        elif not datos:
            print("La base de datos esta vacia!")
        elif data == "4":
            motos = agregar_motos(datos, marcas)
            agregar_datos(motos)
            datos, encabezado = cargar_datos(archivo, separador)    
        elif data == "2":
            sub_opciones()
            mostrar_datos(datos, encabezado)
        elif data == '3':
            obtener_tres_motos_mas_caras_por_marca(datos)
        elif data == '5':
            marca = validar_marca(marcas)
            exportar = motos_x_marca(datos,marca)
            exportar_datos(marca, separador, exportar, encabezado)
        elif data == '6':
            datos, carrito = carrito_motos(datos, encabezado)
            if carrito:
                exportar_datos("Recibo", separador, carrito, encabezado)
                actualizar_datos(archivo, separador, encabezado, datos)
                datos, encabezado = cargar_datos(archivo, separador)

if __name__ == "__main__":
    archivo = "inventario.csv"
    separador = ";"
    menu()
