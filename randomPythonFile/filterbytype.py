#for keys in mydic:
    #print type(mydic [keys])

        #if keys in mydic == type(int)  "this was my original code"
        #    if keys >= 100:                "after this is the fixed code"
        #        print ("That's a big number")
        #        if keys < 100:
        #            print ("small number")


sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']
mydic = {"sI": sI, "mI": mI, "bI": bI, "eI": eI, "spI": spI, "sS": sS, "mS": mS, "bS": bS, "eS": eS, "aL": aL, "mL": mL, "lL": lL, "eL": eL}
for keys in mydic:
    print type(mydic [keys])

    if type(mydic[keys]) is int:
        if mydic[keys] >= 100:
            print ("That's a big number")
        if mydic[keys] < 100:
            print ("small number")

    if type(mydic[keys]) is str:
        if len(mydic[keys]) >= 50:
            print ("big sentence")
        if len(mydic[keys]) < 50:
            print ("small sentence")

    if type(mydic[keys]) is list:
        if len(mydic[keys]) >= 10:
            print ("big list boy")
        if len(mydic[keys]) < 10:
            print ("small list boy")
