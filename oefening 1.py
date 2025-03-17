tijd = "ochtend"
dieet = "vegetarisch"
if tijd == "ochtend":
  if dieet == "vegetarisch":
    print("Je kunt havermout met fruit eten.")
    print("Een smoothie met noten is ook een goede keuze.")
  else:
    print("Een omelet met spek is een stevige start van de dag.")
elif tijd == "middag":
  if dieet == "vegetarisch":
    print("Een salade met geitenkaas en walnoten is een gezonde keuze.")
  else:
    print("Een kipfilet met rijst en groenten is een voedzame lunch.")
else:
  if dieet == "vegetarisch":
    print("Je kunt een groentestoofpot proberen.")
  else:
    print("Een biefstuk met aardappelen is een stevige maaltijd.")