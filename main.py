from core.engine import Engine
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

def main():
    engine = Engine()

    # Registrar comandos
    engine.register_command("saludo", saludo)
    engine.register_command("hora", hora)
    engine.register_command("clear", limpiar)
    engine.register_command("navegador", navegador)

    while True:
        comando = input(">> ").lower()

        if comando == "salir":
            print("Apagando C.O.B.R.A.")
            break

        resultado = engine.execute(comando)
        print(resultado)

if __name__ == "__main__":
    main()
