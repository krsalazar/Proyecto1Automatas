import ply.lex as lex
import re, codecs, os, sys

#Creamos la lista de los tokens que va a usar el lenguaje
#Le indicamos las palabras reservadas que tiene el lnguaje, para que no las tome por variables
reservadas = ['WHILE', 'TRUE', 'IF','SWITCH', 'CASE', 'CIN','COUT']

tokens = reservadas + [
    'ID', 'numero', 'mas', 'menos', 'multi', 'divide', 'punto', 'coma', 'igual'
]

#Ahora un diccionario con las palabras reservadas del lenguaje
'''reservadas = {
    'if':'Control',
    'while':'Ciclo',
    'switch':'Opciones',
    'int':'Entero',  
    'True':'Veradero'
}'''

#tokens = tokens + list(reservadas.values())

#Creamos los tokens que va a usar el lenguaje
t_ignore = '\t'
t_mas = r'\+'
t_menos = r'\-'
t_multi = r'\*'
t_divide = r'/'
t_punto = r'\.'
t_coma = r'\,'
t_igual = r'='

#Para reconocer los nombres de variables, lo hacemos dentro de una función, no como un token mas

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value

    return t

def t_newLine(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#Ahora una función para reconocer los comentarios
def t_comment(t):
    r'\#.*'
    pass

#Ahora la funcion para reconocer numeros
def t_numero(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("Caracter no permitido " + t.value[0])
    t.lexer.skip(1)

#Esta funcion nos permite abrir el directorio seleccionado y escoger el archivo que vamos a leer
def buscarFicheros(directorio):
    ficheros = []
    numArch = ''
    respuesta = False
    cont = 1

#Recorremos el directorio para seleccionar el archivo
    for base, dirs, files in os.walk(directorio, topdown=False):
        ficheros.append(files)
    
    for file in files:
        print(str(cont) + '. ' + file)
        cont+=1
        
    while respuesta == False:
        numArch = input('Numero del archivo a subir\n')
        for file in files:
            if file == files[int(numArch)-1]:
                respuesta = True
                break
    print('Archiivo seleccionado: '+ files[int(numArch)-1])
    
    return files[int(numArch)-1]

#Hay que cambiar la ruta del archivo para que lo pueda leer después
directorio = '.'
archivo = buscarFicheros(directorio)
prueba = archivo
#Codecs permite leer tildes y Ñ en un archivo
fo = codecs.open(prueba, "r", "utf-8")
cadena = fo.read()
fo.close()

analizador = lex.lex()

analizador.input(cadena)

while True:
    tok = analizador.token()
    if not tok : break
    print(tok)