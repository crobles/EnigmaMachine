from os import system

#definicion de constantes 
componenteOrdenada = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
co = componenteOrdenada.split(" ")

reflector = 'A B C D E F G D I J K G M K M I E B F T C V V J A T'
rf = reflector.split(" ")

str_r_derecha = 'B D F H J L C P R T X V Z N Y E I W G A K M U S Q O'
rotorDerecha = str_r_derecha.split(" ")

str_r_medio = 'A J D K S I R U X B L H W T M C Q G Z N P Y F V O E'
rotorMedio = str_r_medio.split(" ")

str_r_izq = 'E K M F L G D Q V Z N T O W Y H X U S P A I B R C J'
rotorIzquierdo = str_r_izq.split(" ")

cilindroDerecho = []
cilindroMedio = []
cilindroIzquierdo = []
listaInput = ""
listaOutput = ""
llaveDiaria = ""
contDer = 0
contMed = 0
contIzq = 0


def creaCilindros():
    for i in zip(co, rotorDerecha):
        cilindroDerecho.append([i[0], i[1]])
    for i in zip(co, rotorMedio):
        cilindroMedio.append([i[0], i[1]])
    for i in zip(co, rotorIzquierdo):
        cilindroIzquierdo.append([i[0], i[1]])
    
        
def ordenaCilindros():
    global llaveDiaria
    arrLlave = llaveDiaria.split("-")
    statIzq = True
    statMed = True
    statDer = True
    while (statIzq == True) or (statMed == True) or (statDer == True):
        #cilindro izq
        dataMoveIz = cilindroIzquierdo[0]
        if dataMoveIz[0] != arrLlave[0]:
            cilindroIzquierdo.pop(0)
            cilindroIzquierdo.append(dataMoveIz)
        else:
            statIzq = False
        #cilindro med
        dataMoveMed = cilindroMedio[0]
        if dataMoveMed[0] != arrLlave[1]:
            cilindroMedio.pop(0)
            cilindroMedio.append(dataMoveMed)
        else:
            statMed = False
        #cilindro der
        dataMoveDer = cilindroDerecho[0]
        if dataMoveDer[0] != arrLlave[2]:
            cilindroDerecho.pop(0)
            cilindroDerecho.append(dataMoveDer)
        else:
            statDer = False
            
def mueveCilindros():
    global contDer
    global contMed
    global contIzq
    dataMoveDer = cilindroDerecho[0]
    cilindroDerecho.pop(0)
    cilindroDerecho.append(dataMoveDer)
    contDer+=1
    if contDer == 26:
        contDer = 0
        dataMoveMed = cilindroMedio[0]
        cilindroMedio.pop(0)
        cilindroMedio.append(dataMoveMed)
        contMed+=1
        if contMed == 26:
            contMed = 0
            dataMoveIzq = cilindroIzquierdo[0]
            cilindroIzquierdo.pop(0)
            cilindroIzquierdo.append(dataMoveIzq)
            contIzq+=1
            if contIzq == 26:
                contIzq = 0

def calculoCilindro(letra):
    posTeclado = None
    posCilDer = None
    posCilMed = None
    posCilIzq = None
    posReflec = None
    #de viaje al reflector
    posTeclado = co.index(letra)
    letraCilDer = cilindroDerecho[posTeclado][1]
    
    for index, n in enumerate(cilindroDerecho):
        if n[0] == letraCilDer:
            posCilDer = index
    
    letraCilMed = cilindroMedio[posCilDer][1]
    
    for index, n in enumerate(cilindroMedio):
        if n[0] == letraCilMed:
            posCilMed = index
            
    letraCilIzq = cilindroIzquierdo[posCilMed][1]
    
    for index, n in enumerate(cilindroIzquierdo):
        if n[0] == letraCilIzq:
            posCilIzq = index
            
    letraReflec = rf[posCilIzq]
    
    for index, n in enumerate(rf):
        if (n == letraReflec) and (index != posCilIzq):
            posReflec = index
            
    #de viaje al teclado
    
    letraCilIzq = cilindroIzquierdo[posReflec][0]
    
    for index, n in enumerate(cilindroIzquierdo):
        if n[1] == letraCilIzq:
            posCilIzq = index
            
    letraCilMed = cilindroMedio[posCilIzq][0]
    
    for index, n in enumerate(cilindroMedio):
        if n[1] == letraCilMed:
            posCilMed = index
    
    letraCilDer = cilindroDerecho[posCilMed][0]
    
    for index, n in enumerate(cilindroDerecho):
        if n[1] == letraCilDer:
            posCilDer = index
            
    letraTeclado = co[posCilDer]
    
    return letraTeclado

def creaLlaveDiaria():
    contador = 1
    diccionario = {1: "primera", 2: "segunda", 3: "tercera"}
    global llaveDiaria
    print("\nDebes ingresar 3 letras para crear tu llave diaria\n")
    while contador <=3:
        letra = input("Por favor ingrese la "+diccionario[contador]+" letra para tu llave: ").upper()
        if contador <3:
            llaveDiaria = llaveDiaria+letra+"-"
        else:
            llaveDiaria = llaveDiaria+letra
        contador = contador + 1
    

def imprimeCilindros():
    print("\n")
    print("Reflector  Rotor_izd   Rotor_med   Rotor_der   Teclado  \n")
    for index, n in enumerate(rf):
        print(
              "    "+n
              +"        ["+cilindroIzquierdo[index][0]+"-"+cilindroIzquierdo[index][1]+"]"
              +"       ["+cilindroMedio[index][0]+"-"+cilindroMedio[index][1]+"]"
              +"       ["+cilindroDerecho[index][0]+"-"+cilindroDerecho[index][1]+"]"
              +"        "+co[index]
        )
    
def main():
    menu = 1
    global listaInput
    global listaOutput
    creaCilindros()
    creaLlaveDiaria()
    ordenaCilindros()
    while menu > 0:
        system("cls")
        print("\n Tu llave diaria es: "+ llaveDiaria+", los cilindros inician en ese orden")
        imprimeCilindros()
        if listaInput != "":
            print("\nTus letras son: "+listaInput)
            print("\nLa salida es: "+listaOutput)
        letraInput = input("\nPor favor ingrese una letra para cifrar o cero para salir: ").upper()
        print(letraInput)
        if letraInput == "0":
            menu = 0
            exit(1)
        mueveCilindros()
        letraTeclado = calculoCilindro(letraInput)
        listaInput= listaInput+" "+letraInput
        listaOutput = listaOutput+" "+letraTeclado

main()
