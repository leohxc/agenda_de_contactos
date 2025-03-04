# Agenda de contactos
# Con función de búsqueda, inserción, actualización y eliminación de contactos.
# Sólo por terminal.

contactos = {}

# Función para agregar información al diccionario de contactos.
def agregar_contacto():
    nombre = input("Ingrese nombre: ")
    apellido= input("Ingrese apellido: ")
    correo = input("Ingrese mail: ")
    teléfono = input("Ingrese teléfono: ")
    contactos[nombre] = {'apellido': apellido, 'correo': correo, 'teléfono': teléfono}

# Función para buscar datos en la agenda.
def buscar_contacto():
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    for contacto, datos in contactos.items():
        if datos['apellido'] == apellido and contacto == nombre:
            print(f"Los datos de {nombre} {apellido} son: Correo: {datos['correo']}, Teléfono: {datos['teléfono']}")
            return
    print("Ese contacto no se encuentra registrado.")

# Función para eliminar contactos de la agenda.
def eliminar_contacto():
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    if nombre in contactos and contactos[nombre]['apellido'] == apellido:
        del contactos[nombre]
        print("Contacto eliminado.")
    else:
        print("Ese contacto no se encuentra registrado.")

# Función para modificar contactos de la agenda.
def update_contacto():
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    if nombre in contactos and contactos[nombre]['apellido'] == apellido:
        correo = input("Ingrese nuevo correo: ")
        teléfono = input("Ingrese nuevo teléfono: ")
        contactos[nombre] = {'apellido': apellido, 'correo': correo, 'teléfono': teléfono}
        print("Contacto actualizado.")
    else:
        print("Ese contacto no se encuentra registrado.")

def mi_agenda():
    
    while True :
        # Con esta condición buscamos que todo se repita de manera infinita.
        print("1. Agregar nuevo contacto") #
        print("2. Lista de contactos") #
        print("3. Modificar contacto existente")
        print("4. Eliminar contacto") #
        print("5. Buscar contacto") #
        print("6. Salir del sistema") # 
        
        option = input("Seleccioná una opción: ")
        
        match option:
            case "1":
                agregar_contacto()
                print("Nuevo contacto ingresado.")
                pass
            case "2":
                print(contactos.items())
                pass
            case "3":
                update_contacto()
                pass
            case "4":
                eliminar_contacto()
                pass
            case "5":
                buscar_contacto()
                pass
            case "6":
                print("Saliendo del sistema. Hasta luego.")
                break # Hasta acá funciona nuestro bucle.
            case _:
                print("Opción no válida. Escribí otra opción del 1 al 5 o 6 para salir del sistema")
mi_agenda()