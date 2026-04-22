from core.engine import Engine
import os
def saludo():
    return "Hola, soy C.O.B.R.A."
def hora():
    return os.popen("date").read()
def main():
    engine = Engine()

    # Registrar comando
    engine.register_command("saludo", saludo)
    engine.register_command("hora", hora)
    while True:
        comando = input(">> ").lower()

        if comando == "salir":
            print("Apagando C.O.B.R.A.")
            break

        resultado = engine.execute(comando)
        print(resultado)

if __name__ == "__main__":
    main()
import os
