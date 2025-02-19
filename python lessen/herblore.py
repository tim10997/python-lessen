guam = int(input("number of guams: "))
marrentill = int(input("number of marrentills: "))
tarromin = int(input("number of tarromins: "))
harralander = int(input("number of harralanders: "))
ranarr = int(input("number of ranarrs: "))
toadflax = int(input("number of toadflaxes: "))
irit = int(input("number of irits: "))
avantoe = int(input("number of avantoes: "))
guam_exp = guam * 25
marrentill_exp = marrentill * 37.5
tarromin_exp = tarromin * 55
harralander_exp = harralander * 67.5
ranarr_exp = ranarr * 87.5
toadflax_exp = toadflax * 80
irit_exp = irit * 100
avantoe_exp = avantoe * 117.5
total_exp = [guam_exp, marrentill_exp, tarromin_exp, harralander_exp, ranarr_exp, toadflax_exp, irit_exp, avantoe_exp]
total_exp = sum(total_exp)
print("total exp to be made: " + str(total_exp))
exp_goal = int(input("total exp needed: "))
print("exp needed is: " + str(exp_goal))
print("exp left is: " + str(exp_goal - total_exp))
