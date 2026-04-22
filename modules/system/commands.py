import os

def saludo():
    return "Hola, soy C.O.B.R.A."

def hora():
    return os.popen("date").read()

def limpiar():
    os.system("clear")
    return ""

def navegador():
    os.system("firefox &")
    return "Abriendo navegador"
