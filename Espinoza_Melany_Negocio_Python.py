def calcular_factura(pedido, cantidad):
    if pedido == 1:
        factura = 2.50 * cantidad
    elif pedido == 2:
        factura = 2.50 * cantidad
    elif pedido == 3:
        factura = 2.50 * cantidad
    elif pedido == 4:
        factura = 2.00 * cantidad
    elif pedido == 5:
        factura = 2.50 * cantidad
    elif pedido == 6:
        factura = 2.75 * cantidad
    elif pedido == 7:
        factura = 3.50 * cantidad
    elif pedido == 8:
        factura = 4.00 * cantidad
    elif pedido == 9:
        factura = 3.75 * cantidad
    else:
        factura = 0
    return factura


def aplicar_descuento(total):
    if total >= 15:
        descuento = total * 0.10
        total = total - descuento
        print("Felicidades, obtuviste un descuentito del 10% uwu")
    return total


def metodo_pago(opcion):
    if opcion == 1:
        mensaje = "Pago hecho con tarjeta"
    elif opcion == 2:
        mensaje = "Pago hecho con efectivo"
    elif opcion == 3:
        mensaje = "Pago hecho con transferencia"
    else:
        mensaje = "No elegiste ningún método :("
    return mensaje


def encuesta_satisfaccion(encuesta):
    if encuesta == 1:
        mensaje = "Muchas gracias <3 Nos alegra que disfrutara su experiencia."
    elif encuesta == 2:
        mensaje = "Gracias por su linda opinión :3 seguiremos mejorando..."
    elif encuesta == 3:
        mensaje = "Trabajaremos para hacerlo mejor ^3^"
    elif encuesta == 4:
        mensaje = "Lamentamos su experiencia T_T"
    else:
        mensaje = "Gracias por responder."
    return mensaje

total = 0
print("/////////////////////////////////////////////////////")
print("..............Cherry Blossom Bytes <3 ...............")
print("...........dulzura que florece contigo...............")
print("*****************************************************")
print("...........Bienvenido a nuestro mundo................")
print("*****************************************************")
print("Desea realizar algún pedido? :3")
print("1. Sí lo deseo")
print("2. No lo deseo gracias")
op = int(input(""))

if op == 1:
    while True:
        print("****************************************************")
        print(".................Nuestro menú :3....................")
        print("****************************************************")
        print("//////////////////////Mochis////////////////////////")
        print("1. Mochi de fresa...............................2.50")
        print("2. Mochi de oreo................................2.50")
        print("3. Mochi de avellana............................2.50")
        print("///////////////////Dorayakis////////////////////////")
        print("4. Dorayaki de chocolate........................2.00")
        print("5. Dorayaki de Nutella..........................2.50")
        print("6. Dorayaki de dulce de leche...................2.75")
        print("///////////////////Bubble Tea///////////////////////")
        print("7. Bubble Tea fresa.............................3.50")
        print("8. Bubble Tea matcha............................4.00")
        print("9. Bubble Tea mango.............................3.75")
        print("*****************************************************")
        pedido = int(input("Por favor escoja su producto favorito <3: "))
        cantidad = int(input("Ingrese la cantidad que desea :3: "))

        if pedido == 1:
            orden = "Mochi de fresa"
        elif pedido == 2:
            orden = "Mochi de Oreo"
        elif pedido == 3:
            orden = "Mochi de Avellana"
        elif pedido == 4:
            orden = "Dorayaki de chocolate"
        elif pedido == 5:
            orden = "Dorayaki de Nutella"
        elif pedido == 6:
            orden = "Dorayaki de dulce de leche"
        elif pedido == 7:
            orden = "Bubble Tea Fresa"
        elif pedido == 8:
            orden = "Bubble Tea Matcha"
        elif pedido == 9:
            orden = "Bubble Tea Mango"
        else:
            orden = "Producto no válido"

        factura = calcular_factura(pedido, cantidad)

        print("Desea confirmar o cancelar el pedido? U_U")
        print("1. Confirmo mi pedido :-3")
        print("2. Cancelo mi pedido >.<")
        confirmar = int(input(""))
        if confirmar == 1:
            total = total + factura
            print("Pedido confirmado correctamente")
            print("****************** SU FACTURA OwO ******************")
            print("Producto:", orden)
            print("Cantidad:", cantidad)
            print("Subtotal:", factura)
            print("Total acumulado:", total)
        else:
            print("No se preocupe, pedido cancelado correctamente =P")

        print("Desea agregar otro producto?")
        print("1. Sí")
        print("2. No")
        continuar = int(input(""))
        if continuar == 2:
            break

    print("Total de su comprita:", total)
    total = aplicar_descuento(total)
    print("Nuevo total a pagar:", total)
    print("Seleccione su método de pago :3")
    print("1. Pago con tarjeta")
    print("2. Pago con efectivo")
    print("3. Pago con transferencia")
    opcion_pago = int(input(""))
    print(metodo_pago(opcion_pago))

    print("******************* ENCUESTA DE SATISFACCIÓN <3 *****************")
    print("1. Estoy enamorada/o de este lugar volvería 100 veces :3")
    print("2. Todo estuvo super lindo y la atención también >.<")
    print("3. Hay cositas que mejorar :)")
    print("4. No me gustó la experiencia")
    encuesta = int(input(""))

    print(encuesta_satisfaccion(encuesta))
    print("...................................................................................")
    print("<<3 Gracias por visitar Cherry Blossom Bytes, esperamos verte de nuevo por aquí <<3")
    print("...................................................................................")
else:
    print("Entendido muchas gracias bonito día ;3")