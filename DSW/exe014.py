class MinhaCasaMinhaVida:
    def __init__(self, bum, saldo):
        self.bum = bum
        self.__saldo = saldo
        
    def depositar(self, valor):
        self.__saldo += valor
        
    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("saldo insuficiente")
            
    def obter_saldo(self):
        return self.__saldo
    
contComi = MinhaCasaMinhaVida("BolsaFamilia", 1000)
print(contComi.bum)
print(contComi.obter_saldo())

contComi.depositar(2500)
print(contComi.obter_saldo())

contComi.sacar(500)
print(contComi.obter_saldo())
