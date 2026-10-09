import primo
import potenze
import area
import casuale
import perimetro
def mostra_menu():
    print()
    print("====== UTILITY CENTER ======")
    print()
    print("1) Verifica se un numero è primo")
    print("2) Calcola quadrato e numero di un cubo")
    print("3) Calcola l'area di un cerchio")
    print("4) Genera un numero casuale")
    print("5) Calcola il perimetro di un poligono") 
    print("6) Esci")
    print()

def main():
    while True:
        mostra_menu()
        try:
            scelta = int(input("Scegli un programma: "))
        except ValueError:
            print()
            print("Devi inserire un valore numerico")
            print()
            continue

        if scelta == 6:
            print("Grazie per aver utilizzato Tool Kit!!!!")
            break

        elif scelta == 1:
            try:
                numero = int(input("Inserisci un numero per sapere se è un numero primo: "))
            except ValueError:
                print("Inserisci un valore numerico")
                continue
            result = primo.primo(numero)
            if result:
                print(f"{numero} è un numero primo")
            else:
                print(f"{numero} non è un numero primo")
                   

        elif scelta == 2:
            try:
                numero = int(input("Inserisci il numero che vuoi elevare al quadrato e al cubo: "))
            except ValueError:
                print("ERRORE: Devi inserire un numero intero")
                continue
            quadrato, cubo = potenze.calcola_potenze(numero)
            print(f"Il quadrato di {numero} è {quadrato}")
            print(f"Il cubo di {numero} è {cubo}")

        elif scelta == 3:
            try:
                raggio = float(input("Inserisci il del cerchio per cerchio per conoscerne l'area: "))
            except ValueError:
                print("ERRORE: Inserisci un valore numerico")
                continue
            if raggio < 0:
                raggio = print(" ERRORE: il raggio non può essere negativo")
                continue
            calcolo = area.calcolo_area(raggio)
            print(f"L'area del cerchio con raggio {raggio} è di {calcolo:.2f}")

        elif scelta == 4:
            input("Premi Invio per generare un numero casuale da 1 a 100... ")
            numero = casuale.num_casuale()
            print(f"Il numero casuale uscito è il numero {numero} ")

        elif scelta == 5:
            perim = 0 
            n = 0
            while n < 3:
                n = int(input("Quanti lati ha il poligono?: "))

            x1 = perimetro.leggi_float("Inserisci la cordinata x del primo punto: ")
            y1 = perimetro.leggi_float("Inserisci la cordinata y del primo punto: ")

            x0 = x1
            y0 = y1

            for i in range(2, n+1):
                x2 = perimetro.leggi_float(f"Inserisci la cordinata x del { i } punto: ")
                y2 = perimetro.leggi_float(f"Inserisci la cordinata y del { i } punto: ")

                perim += perimetro.distanza(x1,y1,x2,y2)
                

                x1 = x2
                y1 = y2 

            perim += perimetro.distanza(x1,y1,x0,y0)

            print(f"Il poligono ha { n } lati e il suo perimetro misura {perim:.2f}")

        else: 
            print()
            print("Scelta non valida")
            print()





   

main()

            

            




