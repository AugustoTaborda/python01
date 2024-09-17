class Animal:
    def __init__(self, name, especie):
        self.name = name
        self.especie = especie
        
    def Faz_o_L(self):
        print(f"{self.name} quem faz o L")
        
cachorro = Animal("patrick", "Marcio")
gato = Animal("Comi", "quem leu")

print(f"{cachorro.name} é um cachorro")
print(f"{gato.name} quem ta lendo")

cachorro.Faz_o_L() 
gato.Faz_o_L()


#Herança

class Cachorro(Animal):
    def Faz_o_L(self):
            print(f'{self.name} quem geme')
            
            
print("faz o L")
cachorro = Cachorro("faz o L", "Comi quem faz o L")
cachorro.Faz_o_L()

#classe

class Gato(Animal):
    def Faz_o_L(self):
         print(f"{self.name} ak47 a arma perfeita para o combate")
         
print("n fala mal do meu prefeito")
gato = Gato("faz o 13", "Ak47")
gato.Faz_o_L()



Animais = [Cachorro("Durex","Cachorra"), Gato("Penolongo", "Desgraça")]

for animal in Animais:
    animal.Faz_o_L()
    
    
    