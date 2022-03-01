class VetorOrdenado:
    def __init__(self, tamanho):
        self.numeroElementos = 0
        self.cidades = [None] * tamanho
        
    def inserir(self, cidade):
        if self.numeroElementos == 0:
            self.cidades[0] = cidade
            self.numeroElementos = 1
            return
        
        posicao = 0
        i = 0
        
        # Percorrer o vetor e encontrar a posição de inserção
        while i < self.numeroElementos:
            if cidade.distancia > self.cidades[posicao].distancia:
                posicao += 1
            i += 1
            
        for k in range(self.numeroElementos, posicao, -1):
            self.cidades[k] = self.cidades[k-1]
            
        self.cidades[posicao] = cidade
        self.numeroElementos += 1
            
    def getPrimeiro(self):
        return self.cidades[0]
    
    def mostrar(self):
        for i in range(0, self.numeroElementos):
            print("{} - {}km".format(self.cidades[i].nome, self.cidades[i].distancia))
            
from Mapa import Mapa
            
vetor = VetorOrdenado(10)
vetor.inserir(Mapa.saoMateus)
vetor.inserir(Mapa.portoUniao)
vetor.inserir(Mapa.lapa)
vetor.mostrar()

'''
Lapa - 74km
São Mateus do Sul - 123km
Porto União - 203km
'''        
        
        
        