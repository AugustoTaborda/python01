with open("exempli.txt", "w") as arquivo:
    arquivo.write("oque tu que ta mole!")
    
with open("exempli.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)