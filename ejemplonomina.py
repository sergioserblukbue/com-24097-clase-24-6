#programa para gestionar una nomina de empleados, con las funciones de leer, crear, actualizar y eliminar empleados.
#los datos se guardan en un archivo empleados.json
#los datos a manejar son nombre, apellido,dirrecion,  legajo, salario,lista de hijos, fecha de nacimiento, fecha de ingreso, fecha de egreso, estado civil
import json
from datetime import datetime
fileName=("./data/empleados.json")
def menu():
    print("1. Leer")
    print("2. Crear")
    print("3. Actualizar")
    print("4. Eliminar")
    print("5. buscar por nombre")
    print("6. buscar por legajo")
    print("7. listar ordenado por apellido")
    print("8. salir")
    try:
        option = int(input("Seleccione una opción: "))
        return option
    except:
        print("Opción no válida")
        return 0
def read():
    try:
        with open(fileName, "r") as file:
            data = json.load(file)
            print(data)
            return data
    except:
        e=Exception
        print(f"No se pudo leer el archivo '{fileName}' error: {e}")
        return []
def listar(data):
    #ordeno por apellido y muestro
    data.sort(key=lambda x: x["apellido"]) #ordeno por apellido usando una funcion lambda para acceder a la clave apellido
    for i in range(len(data)):
        #calculo la edad teniendo en cuenta la fecha actualdel sistema de cada empleado y la muestro en pantalla
        #calculo la edad con la fecha actual del sistema
        #fecha de nacimiento del empleado la tomo del diccionario
        fechaNacimiento=data[i]["fechaNacimiento"]
        #fecha actual del sistema
        fechaActual=datetime.now()
        #calculo la edad
        fechaNacimiento=datetime.strptime(fechaNacimiento, "%d/%m/%Y")
        edad=fechaActual.year-fechaNacimiento.year-((fechaActual.month, fechaActual.day)<(fechaNacimiento.month, fechaNacimiento.day))
        print("listado de empleados".center(70))
        print("="*70)
        print(f"Nombre".ljust(15),f"Apellido".ljust(15),f"Legajo".ljust(15),f"Salario".ljust(15),f"Edad".ljust(15))
        print("-"*70)
        for i in range(len(data)):
            print(data[i]["nombre"].ljust(15),data[i]["apellido"].ljust(15),data[i]["legajo"].ljust(15),data[i]["salario"].ljust(15),str(edad).ljust(15))
        print("-"*70)
        print("Fin del listado".center(70,"="))
      
        
def write(data):
    with open(fileName, "w") as file:
        json.dump(data, file, indent=4)#indent=4 para que se vea tabulado
def create(data):
    allData = read()
    allData.append(data)
    write(allData)
def update(data, index):
    allData = read()
    allData[index] = data
    write(allData)
def delete(index):
    allData = read()
    allData.pop(index)
    write(allData)
def buscarNombre(nombre):
    allData = read()
    for i in range(len(allData)):
        if allData[i]["nombre"]==nombre:
            #muestro los datos del empleado tabulados con encabezados
            print("Nombre".ljust(15), "Apellido".ljust(15), "Direccion".ljust(15), "Legajo".ljust(15), "Salario".ljust(15), "Hijos".ljust(15), "Fecha de Nac".ljust(15), "Ingreso".ljust(15), "Egreso".ljust(15), "Est. Civil".ljust(15))
            print(allData[i]["nombre"].ljust(15), allData[i]["apellido"].ljust(15), allData[i]["direccion"].ljust(15), allData[i]["legajo"].ljust(15), allData[i]["salario"].ljust(15), allData[i]["hijos"].ljust(15), allData[i]["fechaNacimiento"].ljust(15), allData[i]["fechaIngreso"].ljust(15), allData[i]["fechaEgreso"].ljust(15), allData[i]["estadoCivil"].ljust(15))
def buscarLegajo(legajo):
    allData = read()
    for i in range(len(allData)):
        if allData[i]["legajo"]==legajo:
            #muestro los datos del empleado tabulados con encabezados
            print("Nombre".ljust(15), "Apellido".ljust(15), "Direccion".ljust(15), "Legajo".ljust(15), "Salario".ljust(15), "Hijos".ljust(15), "Fecha de Nac".ljust(15), "Ingreso".ljust(15), "Egreso".ljust(15), "Est. Civil".ljust(15))
            print(allData[i]["nombre"].ljust(15), allData[i]["apellido"].ljust(15), allData[i]["direccion"].ljust(15), allData[i]["legajo"].ljust(15), allData[i]["salario"].ljust(15), allData[i]["hijos"].ljust(15), allData[i]["fechaNacimiento"].ljust(15), allData[i]["fechaIngreso"].ljust(15), allData[i]["fechaEgreso"].ljust(15), allData[i]["estadoCivil"].ljust(15))

           
def main():
    while True:
        option=menu()
        if option == 1:
            read()
        elif option == 2:
            data = {
                "nombre": input("Nombre: "),
                "apellido": input("Apellido: "),
                "direccion": input("Direccion: "),
                "legajo": input("Legajo: "),
                "salario": input("Salario: "),
                "hijos": input("Hijos: "),
                "fechaNacimiento": input("Fecha de Nacimiento: "),
                "fechaIngreso": input("Fecha de Ingreso: "),
                "fechaEgreso": input("Fecha de Egreso: "),
                "estadoCivil": input("Estado Civil: ")
            }
            create(data)
        elif option == 3:
            index = int(input("Indice: "))
            #traigo los datos del empleado a actualizar
            allData = read()
            data = allData[index]
            #muestro el nombre actual y pido confirmar si se quiere cambiar
            print(f"Nombre actual: {data['nombre']}")
            confirmar=input("Desea cambiar el nombre? (s/n): ")
            if confirmar.lower()=="s":
                data["nombre"]=input("Nombre: ")
            #muestro el apellido actual y pido confirmar si se quiere cambiar
            print(f"Apellido actual: {data['apellido']}")
            confirmar=input("Desea cambiar el apellido? (s/n): ")
            if confirmar.lower()=="s":
                data["apellido"]=input("Apellido: ")
            #muestro la direccion actual y pido confirmar si se quiere cambiar
            print(f"Direccion actual: {data['direccion']}")
            confirmar=input("Desea cambiar la direccion? (s/n): ")
            if confirmar.lower()=="s":
                data["direccion"]=input("Direccion: ")
            #muestro el legajo actual y pido confirmar si se quiere cambiar
            print(f"Legajo actual: {data['legajo']}")
            confirmar=input("Desea cambiar el legajo? (s/n): ")
            if confirmar.lower()=="s":
                data["legajo"]=input("Legajo: ")
            #muestro el salario actual y pido confirmar si se quiere cambiar
            print(f"Salario actual: {data['salario']}")
            confirmar=input("Desea cambiar el salario? (s/n): ")
            if confirmar.lower()=="s":
                data["salario"]=input("Salario: ")
            #muestro los hijos actuales y pido confirmar si se quiere cambiar
            print(f"Hijos actuales: {data['hijos']}")
            confirmar=input("Desea cambiar los hijos? (s/n): ")
            if confirmar.lower()=="s":
                data["hijos"]=input("Hijos: ")
            #muestro la fecha de nacimiento actual y pido confirmar si se quiere cambiar
            print(f"Fecha de Nacimiento actual: {data['fechaNacimiento']}")
            confirmar=input("Desea cambiar la fecha de Nacimiento? (s/n): ")
            if confirmar.lower()=="s":
                data["fechaNacimiento"]=input("Fecha de Nacimiento: ")
            #muestro la fecha de ingreso actual y pido confirmar si se quiere cambiar
            print(f"Fecha de Ingreso actual: {data['fechaIngreso']}")
            confirmar=input("Desea cambiar la fecha de Ingreso? (s/n): ")
            if confirmar.lower()=="s":
                data["fechaIngreso"]=input("Fecha de Ingreso: ")
            #muestro la fecha de egreso actual y pido confirmar si se quiere cambiar
            print(f"Fecha de Egreso actual: {data['fechaEgreso']}")
            confirmar=input("Desea cambiar la fecha de Egreso? (s/n): ")
            if confirmar.lower()=="s":
                data["fechaEgreso"]=input("Fecha de Egreso: ")
            #muestro el estado civil actual y pido confirmar si se quiere cambiar
            print(f"Estado Civil actual: {data['estadoCivil']}")
            confirmar=input("Desea cambiar el estado civil? (s/n): ")
            if confirmar.lower()=="s":
                data["estadoCivil"]=input("Estado Civil: ")
            #actualizo los datos
            update(data, index)


            
        elif option == 4:
            index = int(input("Indice: "))
            delete(index)
        elif option == 5:
            nombre=input("Nombre: ")
            buscarNombre(nombre)
        elif option == 6:
            legajo=input("Legajo: ")
            buscarLegajo(legajo)
        elif option == 7:
            data=read()
            listar(data)
        elif option == 8:
            break
        else:
            print("Opción no válida")
if __name__ == "__main__":
    main()
    