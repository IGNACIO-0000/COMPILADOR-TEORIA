# Función para limpiar la lista de palabras reservadas eliminando el carácter de nueva línea
def limpiar_lista_reservadas(lista_con_saltos_de_linea):
    """
    Elimina los caracteres de nueva línea al final de cada cadena en la lista.

    Args:
        lista_con_saltos_de_linea (list): Lista de strings que pueden contener '\n' al final.

    Returns:
        list: Una nueva lista de strings sin el carácter '\n' al final.
    """
    lista_limpia = []
    for elemento in lista_con_saltos_de_linea:
        lista_limpia.append(elemento.rstrip('\n'))
    return lista_limpia

# -------------------- ANALIZADORES --------------------

def analisis_lexico(lista_de_lineas):
    """
    Realiza el análisis léxico de una lista de líneas de código fuente.

    Esta función identifica y extrae los tokens del código, ignorando comentarios y espacios en blanco.
    También detecta paréntesis no cerrados.

    Args:
        lista_de_lineas (list): Lista de strings, donde cada string representa una línea del código fuente.

    Returns:
        list: Una lista de tokens identificados en el código fuente.
    """
    lista_depurada = []
    tokens = []
    parentesis_abiertos = 0

    # Primera fase: Depurar comentarios y espacios en blanco
    for linea in lista_de_lineas:
        linea_sin_salto = linea.rstrip('\n')
        if linea_sin_salto.startswith("#") or not linea_sin_salto:
            continue  # Ignorar comentarios y líneas vacías
        lista_depurada.append(linea_sin_salto)

    # Segunda fase: Separar caracteres y formar tokens
    caracteres = []
    for linea in lista_depurada:
        for caracter in linea:
            if caracter != " ":
                caracteres.append(caracter)

    # Tercera fase: Armar tokens y clasificar identidad
    
    print("*** SECUENCIA DE TOKENS ***")
    print("***************************\n")

    recolector_string = ""
    recolector_numeros = ""
    i = 0
    while i < len(caracteres):
        caracter_actual = caracteres[i]

        if caracter_actual == '(':
            parentesis_abiertos += 1
            if recolector_string:
                tokens.append(recolector_string)
                recolector_string = ""
            if recolector_numeros:
                tokens.append(recolector_numeros)
                recolector_numeros = ""
            tokens.append(caracter_actual)
        elif caracter_actual == ')':
            parentesis_abiertos -= 1
            if recolector_string:
                tokens.append(recolector_string)
                recolector_string = ""
            if recolector_numeros:
                tokens.append(recolector_numeros)
                recolector_numeros = ""
            tokens.append(caracter_actual)
        elif caracter_actual in ["=", "+", "-", "*", "/", "[", "]", "."]:
            if recolector_string:
                tokens.append(recolector_string)
                recolector_string = ""
            if recolector_numeros:
                tokens.append(recolector_numeros)
                recolector_numeros = ""
            tokens.append(caracter_actual)
        elif caracter_actual.isdigit():
            recolector_numeros += caracter_actual
        elif caracter_actual.isalpha():
            if recolector_numeros:
                tokens.append(recolector_numeros)
                recolector_numeros = ""
            recolector_string += caracter_actual
        else:
            print(f"Advertencia: Carácter desconocido '{caracter_actual}' ignorado.")

        i += 1

    # Agregar cualquier recolector pendiente al final
    if recolector_string:
        tokens.append(recolector_string)
    if recolector_numeros:
        tokens.append(recolector_numeros)

    if parentesis_abiertos > 0:
        print("\n--- ERROR LÉXICO DETECTADO ---")
        print("Error: Se encontraron paréntesis '(' sin cerrar.")
        return None  # Indica que hubo un error léxico
    elif parentesis_abiertos < 0:
        print("\n--- ERROR LÉXICO DETECTADO ---")
        print("Error: Se encontraron paréntesis ')' de cierre sin apertura.")
        return None  # Indica que hubo un error léxico
    else:
        print(tokens)
        return tokens

def analisis_sintactico(lista_de_tokens):
    """
    Realiza un análisis sintáctico básico de la lista de tokens.

    Esta función intenta identificar la estructura gramatical simple basada en los tokens.

    Args:
        lista_de_tokens (list): Lista de tokens generados por el análisis léxico.

    Returns:
        None
    """
    if lista_de_tokens is None:
        print("\nAnálisis sintáctico omitido debido a errores léxicos.")
        return

    tokens_sintacticos = lista_de_tokens
    almacenamiento_sintactico_tipos = ""
    almacenamiento_sintactico_valores = ""

    print ("\n*** GRAMATICA *** ")
    print ("*****************\n")

    for token in tokens_sintacticos:
        if token in ["x", "y", "z", "w"]:
            almacenamiento_sintactico_tipos += "variable "
            almacenamiento_sintactico_valores += token + " "
        elif token in ["=", "(", ")", "+", "-", "*", "/", "**", "//", "[", "]"]:
            almacenamiento_sintactico_tipos += "operador "
            almacenamiento_sintactico_valores += token + " "
        elif token.isdigit():
            almacenamiento_sintactico_tipos += "num "
            almacenamiento_sintactico_valores += token + " "
        else:
            almacenamiento_sintactico_tipos += "identificador "
            almacenamiento_sintactico_valores += token + " "

    print (almacenamiento_sintactico_tipos ,"\n")
    print (almacenamiento_sintactico_valores)

def analisis_semantico(lista_de_tokens, palabras_reservadas):
    """
    Realiza un análisis semántico básico para detectar errores relacionados con el uso de variables.

    Verifica si las variables se usan antes de ser declaradas (implícitamente en este caso)
    y si se utilizan palabras reservadas como nombres de variables.

    Args:
        lista_de_tokens (list): Lista de tokens generados por el análisis léxico.
        palabras_reservadas (list): Lista de palabras que no pueden ser usadas como nombres de variables.

    Returns:
        None
    """
    if lista_de_tokens is None:
        print("\nAnálisis semántico omitido debido a errores léxicos.")
        return

    variables_declaradas = set()
    errores = []
    i = 0

    print("\n*** ANÁLISIS SEMÁNTICO ***")
    print("***************************\n")

    while i < len(lista_de_tokens):
        token = lista_de_tokens[i]

        # Verifica si es un identificador potencial
        if token.isalpha():
            if token in palabras_reservadas:
                errores.append(f"Error semántico: '{token}' no puede usarse como nombre de variable (palabra reservada).")
            elif i + 1 < len(lista_de_tokens) and lista_de_tokens[i+1] == '=':
                print(f"Declaración: La variable '{token}' ha sido declarada.")
                variables_declaradas.add(token)
            elif token not in variables_declaradas:
                errores.append(f"Error semántico: La variable '{token}' se usó sin ser declarada (implícitamente).")

        i += 1

    if errores:
        print("\n--- ERRORES SEMÁNTICOS DETECTADOS ---")
        for error in errores:
            print(error)
    else:
        print("\nAnálisis semántico exitoso: No se encontraron errores.")

# ***************************************************************************************
# CODIGO FUENTE

try:
    with open("Contenedor_code.txt", "r") as archivo_codigo:
        lista_codigo_fuente = archivo_codigo.readlines()
except FileNotFoundError:
    print("Error: No se pudo encontrar el archivo 'Contenedor_code.txt'")
    exit()

try:
    with open("Palabras_Reservadas.txt", "r") as archivo_reservadas:
        lista_palabras_reservadas_con_salto = archivo_reservadas.readlines()
except FileNotFoundError:
    print("Error: No se pudo encontrar el archivo 'Palabras_Reservadas.txt'")
    exit()

# Lista de palabras reservadas limpias
palabras_reservadas = limpiar_lista_reservadas(lista_palabras_reservadas_con_salto)

# Llamadas de los analizadores
tokens_lexico = analisis_lexico(lista_codigo_fuente)

if tokens_lexico is not None:  # Solo realizar los siguientes análisis si no hubo errores léxicos
    analisis_sintactico(tokens_lexico)
    analisis_semantico(tokens_lexico, palabras_reservadas)
