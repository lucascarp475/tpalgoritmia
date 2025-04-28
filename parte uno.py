datosLocal = """DATOS DEL LOCAL:
Nombre: CiberCafe SA
CUIT: 20123456789
Dirección: Lima 757
Telefono: 1123456789
Mail: cibercafe@gmail.com
"""
menu = """Combos disponibles:
Combo 1: Café + Alfajor $2.500.
Combo 2: Pancho + Gaseosa $4.000.
Combo 3: Hamburguesa + Papas + Gaseosa $7.000.
"""
operacion = 1
#Iniciamos el loop
for i in range(3):
    #Definimos variables por defecto
    valorHoras = 0   #Valor a pagar segun la cantidad de horas elegidas.
    valorComida = 0   #Valor a pagar segun el combo elegido (puede quedar en cero)
    descuento = "Sin descuento" #Define variable descuento por defecto
    servicio = 1
    print("\nBienvenido al Cibercafé")
    nombre = input("Ingrese su nombre: ").title()
    nickname = input("Ingrese su nick: ")
    maquina = input("Elija PC o Consola: ").upper()
    while maquina != "PC" and maquina != "CONSOLA":
        maquina = input("Elija PC o Consola: ").upper()
    if maquina == "PC":
        maquina = "PC"
    if maquina == "CONSOLA":
        maquina = "Consola"

    #Calculo del valor de las horas
    horas = int(input("Cantidad de horas: "))
    while horas != 1 and horas != 2 and horas != 3:
        horas = int(input("Cantidad de horas (máximo 3): "))
    if horas == 1:
        valorHoras = 2500
    elif horas == 2:
        valorHoras = 4000
    elif horas == 3:
        valorHoras = 5550
        
    #Calculo del valor de la comida
    print(menu)
    comida = input("Elija su combo: ").capitalize()
    while comida != "Combo 1" and comida != "Combo 2" and comida != "Combo 3" and comida != "Ninguno":
        comida = input("Elija su combo (Combo 1, Combo 2, Combo 3 o Ninguno): ").capitalize()
    if comida == "Combo 1":
        valorComida = 2500
        comida = str("Café + Alfajor")
    elif comida == "Combo 2":
        valorComida = 4000
        comida = str("Pancho + Gaseosa")
    elif comida == "Combo 3":
        valorComida = 7000
        comida = str("Hamburguesa + Papas + Gaseosa")
    gasto = valorHoras + valorComida    #Gasto total sumando las horas y la comida
    subtotal = valorHoras + valorComida #A diferencia de gasto esta variable no se modifica aplicando los descuentos
    #Calculo del descuento sobre el gasto total
    if gasto > 11500: #Descuento 4%
        gasto = gasto - float((gasto*4/100))
        descuento = str("4%")
    elif gasto > 8000: #Descuento 2%
        gasto = gasto - float((gasto*2/100))
        descuento = str("2%")
    #Facturación
    print(f"\n----------------\nOperación {operacion} \n{datosLocal}\nDATOS DEL CLIENTE: \nNombre: {nombre} \nNickname: {nickname}  \n \nDATOS DEL SERVICIO: \nNumero de servicio: {servicio} \nPC o Consola: {maquina} \nCantoidad de horas: {horas} \nMenú: {comida} \nPrecio del menú: {valorComida} \nSubtotal: {subtotal} \nDescuento: {descuento} \nTOTAL: {gasto}\n----------------")
    operacion = operacion + 1