import math
def distanza(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 -y1)**2)


def leggi_float(messaggio):
    while True:
        try:
            return float(input(messaggio))
        except ValueError:
            print("ERRORE: Inserisci un numero valido!")
