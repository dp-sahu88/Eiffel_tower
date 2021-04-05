#created by:Deviprasad Sahu
print("""🆃🅸🆃🅻🅴: 🅴🅸🅵🅵🅴🅻 🆃🅾🆆🅴🆁
Author: Deͣvⷪiͪpⷥrⷡaⷴsͫaⷥdͫ Saͩhͤuⷭ""")


E = "tE"
materials = ["vA"]*3 +["uC"]*2 +[E,"tBaB",E]+["uC"]*5 +[E]*5+["sG"]*5 +["rI"]*4 +["rBaCaB","qCaCaC"]+["pM"]*2 +["oCbEbC","nCdCdC","mCeCeC"]+["kW"]*2 +["jY","iZA","hZC","gFdKdF","fFgGgF"]+["eFhGhF"]*2

def construct(tower):
    for x in range(len(tower)):
        metal = tower[x].isupper()
        print(("#" if metal else ' ')*(ord(tower[x])-(64 if metal else 96)), end="")
    print()

print ("🇩 🇪 🇦 🇩 🇵 🇴 🇴 🇱 ")
for x in range(len(materials)):
    construct(materials[x])

        
        
print("""🅃🄷🄰🄽🄺🅂 🄵🄾🅁 🄲🄷🄴🄲🄺🄸🄽🄶 🅃🄷🄸🅂 🄲🄾🄳🄴 🄾🅄🅃
               🄳🄴🅅🄸🄿🅁🄰🅂🄰🄳 🅂🄰🄷🅄""")