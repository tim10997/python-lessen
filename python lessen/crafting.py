diamond = int(input("number of uncut diamonds: "))
ruby = int(input("number of uncut rubies: "))
emerald = int(input("number of uncut emeralds: "))
sapphire = int(input("number of uncut sapphires: "))
red_topaz = int(input("number of cut red topazes: "))
jade = int(input("number of cut jades: "))
opal = int(input("number of cut opals: "))
total_gold_gems = [diamond, ruby, emerald, sapphire]
total_silver_gems = [red_topaz, jade, opal]
print("Gold bars needed: " + str(sum(total_gold_gems)))
print("Silver bars needed: " + str(sum(total_silver_gems)))
diamond_exp = diamond * (107.5 + 95)
ruby_exp = ruby * (85 + 80)
emerald_exp = emerald * (67.5 + 65)
sapphire_exp = sapphire * (50 + 60)
total_exp_gold = [diamond_exp, ruby_exp, emerald_exp, sapphire_exp]
print("exp from cutting and gold bracelets: \n", str(sum(total_exp_gold)))
opal_exp = opal * 45
jade_exp = jade * 60
topaz_exp = red_topaz * 75
total_exp_silver = [opal_exp, jade_exp, topaz_exp]
print("exp from silver bracelets: \n", str(sum(total_exp_silver)))
total_exp = sum(total_exp_silver) + sum(total_exp_gold)
print("total exp made: " + str(total_exp))