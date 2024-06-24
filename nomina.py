import json
fileName="./data/nomina.json"
def read():
    try:
        with open(fileName, "r") as file:
            data = json.load(file)
            return data
    except:
        return []
def write(data):
    with open(fileName, "w") as file:
        json.dump(data, file, indent=4)
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
def main():
    while True:
        print("1. Leer")
        print("2. Crear")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Salir")
        option = input("Seleccione una opción: ")
        if option == "1":
            print(read())
        elif option == "2":
            data = {
                "nombre": input("Nombre: "),
                "apellido": input("Apellido: "),
                "salario": input("Salario: ")
            }
            create(data)
        elif option == "3":
            index = int(input("Indice: "))
            data = {
                "nombre": input("Nombre: "),
                "apellido": input("Apellido: "),
                "salario": input("Salario: ")
            }
            update(data, index)
        elif option == "4":
            index = int(input("Indice: "))
            delete(index)
        elif option == "5":
            break
        else:
            print("Opción no válida")
if __name__ == "__main__":
    main()
    