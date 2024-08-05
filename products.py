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
    print("Modificar producto")
    id_producto = input("Introduce el ID del producto a modificar: ")
    title = input("Introduce el nuevo título del producto: ")
    price = float(input("Introduce el nuevo precio del producto: "))
    description = input("Introduce la nueva descripción del producto: ")
    image = input("Introduce la nueva URL de la imagen del producto: ")
    category = input("Introduce la nueva categoría del producto: ")

    producto_actualizado = {
        "title": title,
        "price": price,
        "description": description,
        "image": image,
        "category": category
    }
    
    try:
        url = f'https://fakestoreapi.com/products/{id_producto}'
        respuesta = requests.put(url, json=producto_actualizado)
        if respuesta.status_code == 200:
            print("Producto actualizado")
            print(json.dumps(respuesta.json(), indent=4, ensure_ascii=False))
        elif respuesta.status_code == 404:
            print("No existe el producto con el ID indicado")
        else:
            print(f"Error al actualizar el producto: {respuesta.status_code} {respuesta.text}")
    except Exception as e:
        print(f"Error al actualizar el producto: {e}")

def DeleteProduct():
    print("Eliminación de producto")
    id_producto = input("Introduce el ID del producto a eliminar: ")
    try:
        url = f'https://fakestoreapi.com/products/{id_producto}'
        respuesta = requests.delete(url)
        if respuesta.status_code == 200:
            print("Producto eliminado")
            # La API puede no devolver un contenido JSON en la eliminación, así que puedes omitir json.dumps aquí
        elif respuesta.status_code == 404:
            print("No existe el producto con el ID indicado")
        else:
            print(f"Error al eliminar el producto: {respuesta.status_code} {respuesta.text}")
    except Exception as e:
        print(f"Error al eliminar el producto: {e}")

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
