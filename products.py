import requests
import json

def GetAllProducts():
    try:
        url = 'https://fakestoreapi.com/products'
        respuesta = requests.get(url).json()
        print("Listado de productos")
        print('--------------------')
        print(json.dumps(respuesta, indent=4, ensure_ascii=False))
    except Exception as e:
        print(f"Error al obtener todos los productos: {e}")

def GetProduct():
    print("Búsqueda de producto")
    id_producto = input("Introduce el ID del producto: ")
    try:
        url = f'https://fakestoreapi.com/products/{id_producto}'
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            print(json.dumps(respuesta.json(), indent=4, ensure_ascii=False))
        else:
            print("Producto no encontrado")
    except Exception as e:
        print(f"Error al obtener el producto: {e}")

def AddProduct():
    print("Agregar producto")
    title = input("Introduce el título del producto: ")
    price = float(input("Introduce el precio del producto: "))
    description = input("Introduce la descripción del producto: ")
    image = input("Introduce la URL de la imagen del producto: ")
    category = input("Introduce la categoría del producto: ")

    nuevo_producto = {
        "title": title,
        "price": price,
        "description": description,
        "image": image,
        "category": category
    }

    print("Producto a agregar:", json.dumps(nuevo_producto, indent=4, ensure_ascii=False))

    try:
        url = 'https://fakestoreapi.com/products'
        respuesta = requests.post(url, json=nuevo_producto)
        if respuesta.status_code in [200, 201]:
            print("Producto agregado")
            print(json.dumps(respuesta.json(), indent=4, ensure_ascii=False))
        else:
            print(f"Error al agregar el producto: {respuesta.status_code} {respuesta.text}")
    except Exception as e:
        print(f"Error al agregar el producto: {e}")

def UpdateProduct():
    try:
        id = input("Ingresa el ID del producto a modificar: ")
        url = "https://fakestoreapi.com/products/" + id

        response = requests.get(url)
        if response.status_code == 404:
            print("Producto no encontrado. Por favor, verifica el ID e intenta nuevamente.")
            return  
        elif response.status_code == 200:
            product = response.json()
            if not product:
                print("Producto no encontrado. Por favor, verifica el ID e intenta nuevamente.")
                return

        data = {
            "title": input("Nuevo título: "),
            "price": float(input("Nuevo precio: ")),
            "description": input("Nueva descripción: "),
            "category": input("Nueva categoría: "),
            "image": "https://fakestoreapi.com/img/placeholder.jpg",
        }
        response = requests.put(url, json=data)
        response.raise_for_status()  
        respuesta_json = response.json()
        if respuesta_json is None or "error" in respuesta_json or not respuesta_json:
            print("El producto no existe o no se encontró.")
        else:
            print("Producto actualizado correctamente.")
            print(json.dumps(respuesta_json, indent=4, ensure_ascii=False))
    except requests.exceptions.RequestException as e:
        print("no se pudo actualizar, no existe el producto")



def DeleteProduct():
    print("Eliminación de producto")
    id_producto = input("Introduce el ID del producto a eliminar: ")
    try:
        url = f'https://fakestoreapi.com/products/{id_producto}'
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            print(json.dumps(respuesta.json(), indent=4, ensure_ascii=False))
    except Exception as e:
        print(f"Producto no encontrado")

def mostrar_menu():
    print("\nAdministración de Productos:")
    print("1. Consultar todos los productos")
    print("2. Consultar un producto en específico")
    print("3. Agregar un nuevo producto")
    print("4. Modificar producto en específico")
    print("5. Eliminar un producto")
    print("6. Salir")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-6): ")
    
    if opcion == '1':
        GetAllProducts()
    elif opcion == '2':
        GetProduct()
    elif opcion == '3':
        AddProduct()
    elif opcion == '4':
        UpdateProduct()    
    elif opcion == '5':
        DeleteProduct()
    elif opcion == '6':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, por favor intenta de nuevo.")
