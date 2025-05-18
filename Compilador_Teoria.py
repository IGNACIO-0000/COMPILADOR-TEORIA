# CLEAR PALABRAS RESERVADAS
def CLEAR_LIST_RESERVADAS (LIMPIADOR):
    i = 0
    LIST_CLEAR = []

    while i <= (len(LIMPIADOR) - 1):
        CLEAR = LIMPIADOR[i].rstrip('\n') 
        LIST_CLEAR.append(CLEAR)
        i = i + 1

    return LIST_CLEAR  # RETORNA A LA FUNCION ALASIS LEXICO LA LISTA DE PALABRAS RESERVADAS SIN EL \n 


#ANALIZADORES

#FUNCION ANALISIS LEXICO
def ANALISIS_LIXICO(LIST):
    LIST_IN_LEXICO = LIST
    LIST_DEPURADA = []
    LIST_TOKEN = []
     
    #PRIMERA FASE PARA DEPURAR COMENTARIOS Y ESPACIOS
    
    #CICLO PARA DEPURAR COMENTARIOS Y ESPACIOS EN BLANCO
    CONTADOR_DEPURADOR = 0
    while CONTADOR_DEPURADOR <= (len(LIST_IN_LEXICO)-1): # CICLO PARA ELIMINAR ESPACIOS Y COMENTARIOS

        #CONDICIONES DE UN COMMIT Y UN SPACE

        if LIST_IN_LEXICO[CONTADOR_DEPURADOR][0] == "#" :
            pass
        elif LIST_IN_LEXICO[CONTADOR_DEPURADOR] == "\n":
            pass
          
        else:
            LINEA_DEPURADA = LIST_IN_LEXICO[CONTADOR_DEPURADOR].rstrip('\n') #ELIMINAMOS LOS SALTOS DE LINEA AL FINAL DE UNA CADENA
            LIST_DEPURADA.append(LINEA_DEPURADA) #PROCESO PARA LLENAR LA LISTA LIMPIA

        CONTADOR_DEPURADOR = CONTADOR_DEPURADOR + 1

    #SEGUNDA FASE SEPARAR CARACTERES
    
    LISTA_CARACTERS = [] #LISTA PARA LOS CARACTERES 
    CONTADOR_CHAR_1 = 0
    CONTADOR_CHAR_2 = 0

    while CONTADOR_CHAR_1 <= (len(LIST_DEPURADA)-1):
        while  CONTADOR_CHAR_2 <= (len(LIST_DEPURADA[CONTADOR_CHAR_1])-1): #CONTADOR PARA ELIMINAR ESPACIOS Y ALMACENAR CARACTERES
            if LIST_DEPURADA[CONTADOR_CHAR_1][CONTADOR_CHAR_2] != " ":
                LISTA_CARACTERS.append(LIST_DEPURADA[CONTADOR_CHAR_1][CONTADOR_CHAR_2]) # LISTA CON SOLO CARACTERES
            else:
                pass 
            CONTADOR_CHAR_2 = CONTADOR_CHAR_2 + 1   
        
        CONTADOR_CHAR_2 = 0        
        CONTADOR_CHAR_1 = CONTADOR_CHAR_1 + 1



    #FASE DE ARMAR TOKENS Y CLASIFICACION DE IDENTIDAD 
    TOKEN = []
    CONTADOR_TOKEN = 0
    TOKEN_RECOLECTOR_STRING = ""
    TOKEN_RECOLECTOR_NUMEROS = ""
    
    
    #CICLO PARA CONTRUIR LOS TOKENS

    print("*** SECUENCIA DE TOKENS ***")
    print("""***************************

        """)
    while CONTADOR_TOKEN <= (len(LISTA_CARACTERS)-1):
        
        #CONDICION PARA ALMACENAR OPERADORES
        if(LISTA_CARACTERS[CONTADOR_TOKEN] == "=") or (LISTA_CARACTERS[CONTADOR_TOKEN] == "+") or (LISTA_CARACTERS[CONTADOR_TOKEN] == "-") or (LISTA_CARACTERS[CONTADOR_TOKEN] == "*") or (LISTA_CARACTERS[CONTADOR_TOKEN] == "**") or (LISTA_CARACTERS[CONTADOR_TOKEN] == "//") or (LISTA_CARACTERS[CONTADOR_TOKEN] == "/"):
           TOKEN.append(LISTA_CARACTERS[CONTADOR_TOKEN]) 

        elif(LISTA_CARACTERS[CONTADOR_TOKEN] == ".") or (LISTA_CARACTERS[CONTADOR_TOKEN] == "(") or (LISTA_CARACTERS[CONTADOR_TOKEN] == ")") or (LISTA_CARACTERS[CONTADOR_TOKEN] == "[") or (LISTA_CARACTERS[CONTADOR_TOKEN] == "]"):
            TOKEN.append(LISTA_CARACTERS[CONTADOR_TOKEN])
        
        elif (LISTA_CARACTERS[CONTADOR_TOKEN] == "1") or (LISTA_CARACTERS[CONTADOR_TOKEN] == "2") or (LISTA_CARACTERS[CONTADOR_TOKEN] == "3") or (LISTA_CARACTERS[CONTADOR_TOKEN] == "4") or (LISTA_CARACTERS[CONTADOR_TOKEN] == "5") or (LISTA_CARACTERS[CONTADOR_TOKEN] == "6") or (LISTA_CARACTERS[CONTADOR_TOKEN] == "7") or (LISTA_CARACTERS[CONTADOR_TOKEN] == "8") or (LISTA_CARACTERS[CONTADOR_TOKEN] == "9"):
            TOKEN_RECOLECTOR_NUMEROS += (LISTA_CARACTERS[CONTADOR_TOKEN])
            TOKEN.append(TOKEN_RECOLECTOR_NUMEROS)
        else:
            
            TOKEN_RECOLECTOR_STRING += LISTA_CARACTERS[CONTADOR_TOKEN] 
            TOKEN.append(TOKEN_RECOLECTOR_STRING) 

        CONTADOR_TOKEN += 1
        TOKEN_RECOLECTOR_NUMEROS = ""
        TOKEN_RECOLECTOR_STRING = ""
        print (TOKEN)

            
    return TOKEN

#FUNCION ANALISIS SINTACTICO
def ANALISIS_SINTACTICO(LIST_TOKEN):
        
    #VARIABLES ANALIZADOR SINTACTICO
    TOKEN_SINTACTICO = LIST_TOKEN
    ALMACENAMIENTO_SICTACTICO_1 = ""
    ALMACENAMIENTO_SICTACTICO_2 = ""
    CONTADOR_SINTACTICO = 0

    #CONSTRUCCION DE LA GRAMATICA TIPO 2
    while CONTADOR_SINTACTICO <= (len(TOKEN_SINTACTICO)-1):

        if (TOKEN_SINTACTICO[CONTADOR_SINTACTICO] == "x") or (TOKEN_SINTACTICO[CONTADOR_SINTACTICO] == "y") or (TOKEN_SINTACTICO[CONTADOR_SINTACTICO] == "z") or (TOKEN_SINTACTICO[CONTADOR_SINTACTICO] == "w"):
            ALMACENAMIENTO_SICTACTICO_1 += "variable "
            ALMACENAMIENTO_SICTACTICO_2 += TOKEN_SINTACTICO[CONTADOR_SINTACTICO]

        elif(TOKEN_SINTACTICO[CONTADOR_SINTACTICO] == "=") or (TOKEN_SINTACTICO[CONTADOR_SINTACTICO] == "(") or (TOKEN_SINTACTICO[CONTADOR_SINTACTICO] == ")"):
            ALMACENAMIENTO_SICTACTICO_1 += "operador "
            ALMACENAMIENTO_SICTACTICO_2 += TOKEN_SINTACTICO[CONTADOR_SINTACTICO]

        elif(TOKEN_SINTACTICO[CONTADOR_SINTACTICO] == "+") or (TOKEN_SINTACTICO[CONTADOR_SINTACTICO] == "-") or (TOKEN_SINTACTICO[CONTADOR_SINTACTICO] == "*"):
            ALMACENAMIENTO_SICTACTICO_1 += "operador "
            ALMACENAMIENTO_SICTACTICO_2 += TOKEN_SINTACTICO[CONTADOR_SINTACTICO]    

        else:
            ALMACENAMIENTO_SICTACTICO_1 += "num "
            ALMACENAMIENTO_SICTACTICO_2 += TOKEN_SINTACTICO[CONTADOR_SINTACTICO]  

        CONTADOR_SINTACTICO += 1

    # MENSAJE DE LA DERIVADA GRAMATICA
    print ("\n","*** GRAMATICA *** ","\n","*****************","\n","\n",ALMACENAMIENTO_SICTACTICO_1 ,"\n","\n",ALMACENAMIENTO_SICTACTICO_2)
             
    return
    #Analizador semantico
     
  def ANALISIS_SEMANTICO(lista_tokens, palabras_reservadas):
    variables_declaradas = set()
    errores = []
    i = 0

    print("\n*** ANÁLISIS SEMÁNTICO ***")
    print("***************************\n")

    while i < len(lista_tokens):
        token = lista_tokens[i]

        # Verifica si es identificador potencial (ni operador ni número)
        if token not in ['=', '+', '-', '*', '/', '(', ')'] and not token.isdigit():
            if token in palabras_reservadas:
                errores.append(f"Error semántico: '{token}' no puede usarse como nombre de variable (palabra reservada).")
            elif i + 1 < len(lista_tokens) and lista_tokens[i+1] == '=':
                print(f"Declaración: La variable '{token}' ha sido declarada.")
                variables_declaradas.add(token)
            elif token not in variables_declaradas:
                errores.append(f"Error semántico: La variable '{token}' se usó sin declararse previamente.")
            else:
                print(f"Uso correcto: La variable '{token}' ha sido usada correctamente.")

        i += 1

    if errores:
        print("\n--- ERRORES SEMÁNTICOS DETECTADOS ---")
        for e in errores:
            print(e)
    else:
        print("\nAnálisis semántico exitoso: No se encontraron errores.")

#***************************************************************************************
#CODIGO FUENTE

#VARIABLES CODIGO
BOOK_CODE = open ("Contenedor_code.txt" , "r") # ABRIMOS EL CODIGO
LIST_BOOK_CODE = BOOK_CODE.readlines() # GUARDAMOS LAS LINEAN EN UN VECTOR

BOOK_PALABRAS_RESERVADAS = open("Palabras_Reservadas.txt" , "r") # ARCHIVO PALABRAS RESERVADAS
LIST_RESERVADAS = BOOK_PALABRAS_RESERVADAS.readlines() #VECTOR PALABRAS RESERVADASbS

#LISTA DE PALABRAS RESERVADAS 
PALABRAS_RESERVADAS = CLEAR_LIST_RESERVADAS(LIST_RESERVADAS)

#LLAMADAS DE ANALIZADORES

TO_GO_LEXICO = ANALISIS_LIXICO(LIST_BOOK_CODE) # ENVIAMOS EL VECTOR A ANALISIS LEXICO
TO_GO_SINTACTICO = ANALISIS_SINTACTICO(TO_GO_LEXICO)
TO_GO_SEMANTICO= ANALISIS_SEMANTICO(TO_GO_LEXICO, PALABRAS_RESERVADAS)

         
BOOK_CODE.close()
BOOK_PALABRAS_RESERVADAS.close()

