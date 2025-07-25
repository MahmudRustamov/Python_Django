""""Berilgan list ni shunday yangilanki, list elementlarining o'rninga shu list elementlarining tiplari joylashib qolsin"""

ls = [True, "Salom", 5, 5.6]
updated_ls = []
for i in ls:
    updated_ls.append(type(i))
print(updated_ls)