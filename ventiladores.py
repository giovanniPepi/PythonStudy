class Eletro: 
    def __init__(self, nome, potencia, horas, dias):
        self.nome = nome
        self.potencia = potencia
        self.horas = horas
        self.dias = dias

    def aboutvent (self):
        print(f"Aparelho {self.nome.title()}, {self.potencia}W, {self.horas} horas diárias utilizadas, {self.dias} dias utilizados.")

    def set_potência (self, potencia):
        self.potencia = potencia

    def set_horas (self, horas):
        self.horas = horas
    
    def set_dias (self, dias):
        self.dias = dias
    
    def consumo (self):
        preçokwh = 1.00
        kwh = ((self.potencia * self.horas * self.dias) / 1000)
        gasto = kwh * preçokwh
        print(f"Aparelho {self.nome.title()}, {self.potencia}W, {self.horas} horas por dia "
        f"{self.dias} dias: R${gasto} em {kwh} KWh")

turbosilence40 = Eletro('philco', 60, 8, 30)
turbosilence40.consumo()
turbosilence40.set_horas(24)
turbosilence40.consumo()

malloryts40 = Eletro('mallory', 126, 8, 30)
malloryts40.consumo()

mondialnv156pfb = Eletro ('mondial', 30, 8, 30)
mondialnv156pfb.consumo() 

mondialnv156pfb.set_horas(24)
mondialnv156pfb.consumo()

gtx1050ti = Eletro('GTX 1050Ti', 64, 24, 30)
gtx1050ti.consumo()

chuveiro3 = Eletro('Chuveiro nível 3', 7500, 0.1, 30)
chuveiro3.consumo()

chuveiro2 = Eletro('Chuveiro nível 2', 5000, 0.1, 30)
chuveiro2.consumo()

chuveiro1 = Eletro('Chuveiro nível 1', 1000, 0.1, 30)
chuveiro1.consumo()

pcidle = Eletro('PC em idle', 150, 24, 30)
pcidle.consumo()

pcfullload = Eletro('PC Full load', 300, 24, 30)
pcfullload.consumo()

pcmiddleload = Eletro('PC middle load sem GPU', 200, 24, 30)
pcmiddleload.consumo()

monitorlgmax = Eletro('Monitor 27" máximo', 43, 8, 30)
monitorlgmax.consumo()

monitorlgmiddle= Eletro('Monitor 27" middle', 36, 8, 30)
monitorlgmiddle.consumo()

monitorlgmin = Eletro('Monitor 27" min', 22, 8, 30)
monitorlgmin.consumo()
