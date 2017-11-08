#Naam: Bram Bosch
#Nummer: 597873
#Klas: BIN-1D

'''
In de functie main roep ik alle functies aan en zorg ik dat alle resulaten
geprint worden.

input: niks
return: niks
'''

def main():
    lijst = read_file()
    lijstCodes,unvalidated = not_validated(lijst)
    lijstIon = ion_involved(lijstCodes,lijst)
    print(60*"-")
    print("Aantal ongeverifieerde genen:", unvalidated)
    print("Aantal genen betrokken bij ion processen:" ,len(lijstIon))
    i=0
    for item in lijstCodes:
        print(60*"-")
        print("Accesie code:                             " ,lijst[item][0])
        if item in lijstIon:
            print("Is het gen betrokken bij een ion proces:   Ja")
        else:
            print("Is het gen betrokken bij een ion proces:   Nee")
        i+=1
        
'''
In de functie read_file wordt het CSV bestand geopend en in een 2D lijst gestopt.

input: niks
return: 2D lijst met de inhoud van het bestand
'''
def read_file():
    file = open("yeast_genes.csv", "r")    
    lijst=[]
    for regel in file:
        regel = regel.replace("\n","")
        regel = regel.split(",")
        lijst.append(regel)
    return lijst

'''
In de functie not_validated er in de grote 2D lijst gekeken naar of het verified is of niet
Alle indexen waarbij het niet verified is worden in een lijst gestopt en er wordt
bij gehouden hoevaak dit gebeurt

input: grote 2D lijst
return: Lijst met indexen en aantal niet geverifieerde genen.
'''

def not_validated(lijst):
    i=0
    lijstCodes = []
    unvalidated = 0
    for item in lijst:
        if lijst[i][1]!= "Verified":
            lijstCodes.append(i)
            unvalidated += 1
        i += 1
    lijstCodes.remove(0)
    #ik haal hier specifiek de waarde 0 weg omdat dit de waarde van de header is 
    return lijstCodes, unvalidated

'''
In de functie ion_involved wordt gekeken of het woord ion voorkomt achter de accesie codes van de niet
geverifieerde genen

input: grote 2D lijst en lijst met de indexen van de niet geverifeerde indexen
return: lijst met indexen waar de niet geverifieerde genen betrekking hebben op een
ion proces
'''

def ion_involved(lijstCodes,lijst):
    i=0
    lijstIon = []
    for item in lijstCodes:
        if "ion" in lijst[item][1:]:
            lijstIon.append(item)
    return lijstIon

main()
