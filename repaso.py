lista_usuarios = {
    'user123': {'nombre': 'sebastian', 'tipo': 'usuario', 'cedula': '12345'},
    'admin123': {'nombre': 'oscar', 'tipo': 'admin', 'cedula': '09876'},
    'german_..': {'nombre': 'german', 'tipo': 'usuario', 'cedula': '2345'}
}

def depositar_dinero():
    dinero_para_depositar = input("Cuanto dinero deseas depositar\n>>> ")
    if dinero_para_depositar <= "1000":
        print("Nose puede depositar tan poco dinero")
    else:
        print("Dinero depositado exitosamente")

def retirar_dinero():
    dinero_para_retirar = input("Cuanto dinero deseas retirar\n>>> ")
    if dinero_para_retirar <= "1000":
        print("Nose puede retirar tan poco dinero")
    else:
        print("Dinero retirado exitosamente")


def servicios(usuario_ingresado):
    print(f"\nBienvenido a tu cuenta {usuario_ingresado}")
    numero_servicios = input("\n1)Depositar Dinero\n2)Retirar Dinero\n3)Consultar Saldo\n>>> ")

    for i in range(1):
        if numero_servicios == "1": depositar_dinero()
        elif numero_servicios == "2": retirar_dinero()
        elif numero_servicios == "3": print("Hola puedes consultar tu saldo")
        else: print("Valor incorrecto")



def validador(usuario):
    intentos = 0
    max_intentos = 3
    
    while intentos < max_intentos:
        contraseña = input("Ingresa tu contraseña\n>>> ")
        
        if contraseña in usuario:
            datos = usuario[contraseña]
            print(f"Hola bienvenido {datos['tipo']} {datos['nombre']}")
            servicios(datos)
            break
        else:
            intentos += 1
            if intentos >= max_intentos:
                print("Numero de intentos maximos alcanzados")
            else:
                print("Contraseña incorrecta")

def main():

    validador(lista_usuarios)

main()