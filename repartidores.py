def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote=lista[0]

        mayor = [x for x in lista[1:] if x[1]['paquetes'] > pivote[1]['paquetes']]
        igual = [x for x in lista[1:] if x[1]['paquetes'] == pivote[1]['paquetes']]
        menor = [x for x in lista[1:] if x[1]['paquetes'] < pivote[1]['paquetes']]

        return quick_sort(mayor) + [pivote] + quick_sort(igual + menor)
def ingreso_repartidores():
    repartidores={}

    while True:
        try:
            n = int(input("Cantidad de repartidores: "))
            if n>0:
                break
            else:
                print("Numero invalido.")
        except ValueError:
            print("Ingrese numero valido.")

    for _ in range(n):
        while True:
            nombre = input("Nombre del repartidor: ").strip()
            if nombre=="":
                print("Debe escribir un nombre.")
            elif nombre in repartidores:
                print("El repartidor ya existente.")
            else:
                break
        while True:
            try:
                paquetes=int(input("Cantidad de paquetes: "))
                if paquetes>=0:
                    break
                else:
                    print("Ingrese cantidad de paquetes.")
            except ValueError:
                print("Ingrese un numero valido.")
        while True:
            zona=input("Zona asignada: ").strip()
            if zona:
                break
            else:
                print("La casilla no puede quedar vacia")
        repartidores[nombre]={"paquetes": paquetes, "zona": zona}
    return repartidores

def mostrar_repartidores(repart):
    lista=list(repart.items())
    orden=quick_sort(lista)
    print("\n ")

