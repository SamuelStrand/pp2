import json

f_path =r"C:\Users\emilv\Documents\GitHub\pp2\labs\lab4\json\js.json"
f = open(f_path)
x = json.load(f)

print("Interface Status\n")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")
for object in x["imdata"]:
    object1 = object["l1PhysIf"]["attributes"]
    print(f'{object1["dn"]}                              {object1["speed"]}   {object1["mtu"]}')