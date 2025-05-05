import random

# Rol twee 6-kantige dobbelstenen.

aantal_worpen = 0
totaal_van_de_worpen = 0
lopende_totaal = 0
hoeveel_worpen = int(iput("hoeveel keer wil je het expiriment uitvoeren"))
while aantal_worpen < hoeveel_worpen:
    eerste_steen = random.randint(1, 6)
    tweede_steen = random.randint(1, 6)
    dobbelsteen_som = eerste_steen + tweede_steen
    print("Je rolde een " + str(dobbelsteen_som) + "!")
    aantal_worpen = aantal_worpen + 1
    lopende_totaal = lopende_totaal + dobbelsteen_som

gem_waarde = lopende_totaal / 10
print("het gemiddelde van de 10 worpen is " + str(gem_waarde))