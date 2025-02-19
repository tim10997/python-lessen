# tayyab & meryem & doaa & (yanis) &
naam = input("hoe heet je?")
aantal_vrienden = int(input("Hoeveel vrienden zullen er zijn?"))
prijs_snacks = int(input("Hoeveel kosten de snacks per persoon?"))
prijs_filmticket = int(input("Hoeveel kost het filmticket per persoon?"))

totale_prijs = aantal_vrienden * prijs_snacks + aantal_vrienden * prijs_filmticket

totale_prijs = str(totale_prijs)
if totale_prijs > "100" : print("Dit wordt een dure avond! Misschien een goedkopere optie overwegen?")

print("Hallo " + naam + " Je zal in totaal voor jij plus jouw "+ str(aantal_vrienden) + " vrienden " + totale_prijs + " euro moeten betalen")

#jaydae en arturo
naam = input("Wat is je naam? ")
aantal_vrienden = int(input("Hoeveel vrienden wil je uitnodigen? "))
float(input("Wat is de prijs per persoon voor snacks? (€) "))
prijs_filmticket = float(input("Wat is de prijs van een filmticket? "))

#mike
naam = input("Wat is uw naam")
aantal_vrienden = int(input("Hoeveel vrienden wilt u uitnodigen"))
prijs_snacks = int(input("Hoeveel kosten de snacks per persoon?"))
prijs_filmticket = int(input("Hoeveel kost het filmticket per persoon?"))

totale_prijs = aantal_vrienden * prijs_snacks + aantal_vrienden * prijs_filmticket

totale_prijs = str(totale_prijs)
if totale_prijs > "100" : print("Dit gaat duur zijn, wilt u een andere optie?")
print("Hallo " + naam + " Dit zal voor jij plus jouw "+ str(aantal_vrienden) + " vrienden " + totale_prijs + " euro kosten")