# =====================================================================
# TEMA 5: Arreglos y Tipos Abstractos de Datos (Parte 1)
# Reto 2: Sistema Básico de Gestión de Pedidos e Inventario
# =====================================================================

# Estructuras de datos globales (Arreglos / Listas de diccionarios)
inventario = [
    {"id": 1, "nombre": "Laptop", "stock": 10, "precio": 850.0},
    {"id": 2, "nombre": "Mouse", "stock": 25, "precio": 25.0}
]

pedidos = [
    {"id_pedido": 101, "cliente": "Juan Pérez", "producto": "Laptop", "cantidad": 1}
]

# =====================================================================
# MÓDULO DE INVENTARIO
# =====================================================================

def mostrar_inventario():
    """Muestra el listado actual de productos en el inventario."""
    print("\n--- LISTADO DE INVENTARIO ---")
    if not inventario:
        print("El inventario está vacío.")
        return
    for item in inventario:
        print(f"ID: {item['id']} | Producto: {item['nombre']} | Stock: {item['stock']} | Precio: ${item['precio']}")

def registrar_producto():
    """Registra un nuevo producto en el arreglo de inventario."""
    print("\n--- REGISTRAR NUEVO PRODUCTO ---")
    try:
        nuevo_id = len(inventario) + 1
        nombre = input("Ingrese el nombre del producto: ")
        stock = int(input("Ingrese la cantidad en stock: "))
        precio = float(input("Ingrese el precio unitario: "))
        
        nuevo_item = {"id": nuevo_id, "nombre": nombre, "stock": stock, "precio": precio}
        inventario.append(nuevo_item)
        print(f"¡Producto '{nombre}' registrado exitosamente con ID {nuevo_id}!")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos para stock y precio.")

def editar_producto():
    """Edita un producto existente en el inventario buscando por su ID."""
    mostrar_inventario()
    try:
        id_buscar = int(input("\nIngrese el ID del producto que desea editar: "))
        for item in inventario:
            if item['id'] == id_buscar:
                print(f"Editando a: {item['nombre']}. Deje en blanco para no cambiar.")
                nuevo_nombre = input(f"Nuevo nombre [{item['nombre']}]: ")
                nuevo_stock = input(f"Nuevo stock [{item['stock']}]: ")
                nuevo_precio = input(f"Nuevo precio [{item['precio']}]: ")
                
                if nuevo_nombre: item['nombre'] = nuevo_nombre
                if nuevo_stock: item['stock'] = int(nuevo_stock)
                if nuevo_precio: item['precio'] = float(nuevo_precio)
                
                print("¡Producto actualizado exitosamente!")
                return
        print("Error: No se encontró un producto con ese ID.")
    except ValueError:
        print("Error: ID inválido.")

def eliminar_producto():
    """Elimina un producto del inventario por su ID."""
    mostrar_inventario()
    try:
        id_buscar = int(input("\nIngrese el ID del producto a eliminar: "))
        for item in inventario:
            if item['id'] == id_buscar:
                inventario.remove(item)
                print(f"¡Producto con ID {id_buscar} eliminado del inventario!")
                return
        print("Error: Producto no encontrado.")
    except ValueError:
        print("Error: ID inválido.")


# =====================================================================
# MÓDULO DE PEDIDOS
# =====================================================================

def mostrar_pedidos():
    """Muestra el listado actual de pedidos registrados."""
    print("\n--- LISTADO DE PEDIDOS ---")
    if not pedidos:
        print("No hay pedidos registrados.")
        return
    for p in pedidos:
        print(f"Pedido ID: {p['id_pedido']} | Cliente: {p['cliente']} | Producto: {p['producto']} | Cantidad: {p['cantidad']}")

def registrar_pedido():
    """Registra un nuevo pedido en el sistema."""
    print("\n--- REGISTRAR NUEVO PEDIDO ---")
    mostrar_inventario()
    try:
        id_ped = len(pedidos) + 101
        cliente = input("Nombre del cliente: ")
        prod_nombre = input("Nombre del producto solicitado: ")
        cantidad = int(input("Cantidad requerida: "))
        
        nuevo_p = {"id_pedido": id_ped, "cliente": cliente, "producto": prod_nombre, "cantidad": cantidad}
        pedidos.append(nuevo_p)
        print(f"¡Pedido #{id_ped} para {cliente} registrado con éxito!")
    except ValueError:
        print("Error: Ingrese una cantidad numérica válida.")

def editar_pedido():
    """Edita un pedido existente."""
    mostrar_pedidos()
    try:
        id_buscar = int(input("\nIngrese el ID del pedido que desea editar: "))
        for p in pedidos:
            if p['id_pedido'] == id_buscar:
                nuevo_cliente = input(f"Nuevo cliente [{p['cliente']}]: ")
                nueva_cant = input(f"Nueva cantidad [{p['cantidad']}]: ")
                
                if nuevo_cliente: p['cliente'] = nuevo_cliente
                if nueva_cant: p['cantidad'] = int(nueva_cant)
                
                print("¡Pedido actualizado exitosamente!")
                return
        print("Error: Pedido no encontrado.")
    except ValueError:
        print("Error: ID inválido.")

def eliminar_pedido():
    """Elimina un pedido del sistema."""
    mostrar_pedidos()
    try:
        id_buscar = int(input("\nIngrese el ID del pedido a eliminar: "))
        for p in pedidos:
            if p['id_pedido'] == id_buscar:
                pedidos.remove(p)
                print(f"¡Pedido #{id_buscar} eliminado!")
                return
        print("Error: Pedido no encontrado.")
    except ValueError:
        print("Error: ID inválido.")


# =====================================================================
# MENÚ PRINCIPAL INTERACTIVO
# =====================================================================
def menu_principal():
    """Controla el flujo del programa mediante un menú modular."""
    while True:
        print("\n========================================")
        print("   SISTEMA DE INVENTARIO Y PEDIDOS")
        print("========================================")
        print("1. Mostrar Inventario")
        print("2. Registrar Producto")
        print("3. Editar Producto")
        print("4. Eliminar Producto")
        print("----------------------------------------")
        print("5. Mostrar Pedidos")
        print("6. Registrar Pedido")
        print("7. Editar Pedido")
        print("8. Eliminar Pedido")
        print("----------------------------------------")
        print("9. Salir")
        
        opcion = input("Seleccione una opción (1-9): ")
        
        if opcion == '1': mostrar_inventario()
        elif opcion == '2': registrar_producto()
        elif opcion == '3': editar_producto()
        elif opcion == '4': eliminar_producto()
        elif opcion == '5': mostrar_pedidos()
        elif opcion == '6': registrar_pedido()
        elif opcion == '7': editar_pedido()
        elif opcion == '8': eliminar_pedido()
        elif opcion == '9':
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo entre 1 y 9.")

if __name__ == "__main__":
    menu_principal()