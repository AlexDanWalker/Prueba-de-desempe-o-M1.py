ACLARACION FUNCION search_product(): EN esta funcion la validacion que indica si el producto esta en el inventario imprime el mensaje "The product {name} is out of stock. Here are the available products:"
pero ademas tambien suelta un listado del inventario actual, a simple vista parece que no hubiera pasado nada por el listado del inventario, pero si abres la terminal lo suficiente el mensaje se veria asi:

Entrada: Pan
Salida:The product Pan is out of stock. Here are the available products:

---List of products available in inventory---
- Pintura
- Pincel
- Martillo
- Taladro



INTRUCCIONES EJECUCION DEL PROGRAMA: 
Requisitos previos:

-Tener instalado Python en tu computadora.
-Copiar el código del programa en un archivo con extensión .py (por ejemplo, inventario.py).

Ejecutar el programa:

Abre una terminal o consola en tu computadora.
Navega hasta el directorio donde guardaste el archivo prueba tecnica M1.
Escribe el comando python prueba tecnica M1.py y presiona Enter.
El programa se ejecutará y mostrará el menú principal.

Uso del programa:

En el menú principal, selecciona una opción ingresando el número correspondiente (1-6).

Sigue las instrucciones para cada opción:
Agregar producto: Ingresa el nombre, precio y cantidad del producto.
Buscar producto: Ingresa el nombre del producto que deseas buscar.
Actualizar producto: Ingresa el nombre del producto que deseas actualizar y los nuevos valores de precio y cantidad.
Eliminar producto: Ingresa el nombre del producto que deseas eliminar y confirma la eliminación.
Calcular valor del inventario: No requiere entrada adicional, solo muestra el valor total del inventario.
Salir: Finaliza el programa.
Para cada opción, el programa mostrará los resultados correspondientes.
Notas

Asegúrate de ingresar los datos correctamente, ya que el programa valida la entrada.
Si ingresas un valor incorrecto, el programa mostrará un mensaje de error y te pedirá que ingreses el valor nuevamente.

Espero que estas instrucciones te ayuden a ejecutar el programa correctamente.



DATOS DE ENTRADA Y SALIDA:

Opción 1: Agregar producto

Entrada:
Nombre del producto: Cemento
Precio: 20
Cantidad: 10
Salida:
"El producto 'Cemento' se ha añadido correctamente."
Lista de productos disponibles actualizada

Opción 2: Buscar producto

Entrada:
Nombre del producto: Pintura
Salida:
"Producto: Pintura - Precio: 30.0 - Cantidad: 5"

Opción 3: Actualizar producto

Entrada:
Nombre del producto: Martillo
Nuevo precio: 18
Nueva cantidad: 5
Salida:
"El producto 'Martillo' ha sido actualizado correctamente."
"Nuevo precio: 18.0, Nueva cantidad: 5"

Opción 4: Eliminar producto

Entrada:
Nombre del producto: Pincel
Confirmación: S
Salida:
"El producto 'Pincel' ha sido eliminado."
Lista de productos disponibles actualizada

Opción 5: Calcular valor del inventario

Entrada: Ninguna
Salida:
"El valor total del inventario es: X USD" (donde X es el valor total del inventario)

Opción 6: Salir

Entrada: Ninguna
Salida:
"Finalizando el programa..."
