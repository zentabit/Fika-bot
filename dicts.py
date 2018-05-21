


with open('../data.txt', encoding='utf8') as f:
    stri = f.read()
things = eval(stri)

print(things)

things[21] = "Axel"

print(things)

with open("../data.txt",'w', encoding='utf8') as f:
    f.write(str(things))