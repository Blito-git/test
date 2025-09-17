titulos=[]
ejemplares=[]
print("MENU\n1. Ingresar lista de titulos\n2. Ingresar lista de ejemplares disponibles\n3. Mostrar catalogo completo\n4. Consultar disponibilidad de un titulo especifico\n5. Lista con stock\n6. Agregar titulo\n7. Ver titulos agotados\n8. Actualizar ejemplares\n9. Ver catalogo\n10. Salir")
opcion=input("Ingrese una opicon: ")
while opcion!="10":
    if opcion=="1":
        n=int(input("Cuantos titulos desea ingresar?: "))
        for i in range(n):
            libro=input("Ingrese el titulo "+str(i+1)+": ")
            titulos.append(libro)
            ejemplares.append(0)
    elif opcion=="2":
        if len(titulos)==0:
            print("Primero debe ingresar titulos (opcion 1)")
        else:
            for i in range(len(titulos)):
                copias=int(input("Ingrese ejemplares disponibles para "+ titulos[i]+": "))
                ejemplares[i]=copias
    elif opcion=="3":
        if len(titulos)==0:
            print("No hay titulos cargados")
        else:
            print("Catalogo completo")
            for i in range(len(titulos)):
                print(titulos[i]+": "+str(ejemplares[i]+" ejemplares"))
    elif opcion=="4":
        titulo_buscar=input("Ingrese el titulo a consultar ")
        if titulo_buscar in titulos:
            i=titulos.index(titulo_buscar)
            print(titulo_buscar+": "+str(ejemplares[i]+"ejemplares disponibles"))
        else:
            print("Titulo no encontrado en catalogo")
    elif opcion=="5":
        print("Lista con stock")
        for i in range(len(titulos)):
            if ejemplares[i]>0:
                print(titulos[i]+": "+str(ejemplares[i])+" ejemplares")
            else:
                print("No hay titulos con stock")
    elif opcion=="6":

    elif opcion=="7":

    elif opcion=="8":

    elif opcion=="9":
