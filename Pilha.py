class Pilha:
  def __init__(self, tamanho):
    self.tamanho = tamanho
    self.cidades = [None] * self.tamanho
    self.topo = -1

  def empilhar(self, cidade):
    if not Pilha.pilhaCheia(self):
      self.topo += 1
      self.cidades[self.topo] = cidade 
    else:
      print("Pilha cheia! Não é possível empilhar")

  def desempilhar(self):
    if not Pilha.pilhaVazia(self):
        temp = self.cidades[self.topo]
        self.topo -= 1
        return temp
    else:
        print("A pilha já está vazia!\n")
        return None 

  def getTopo(self):
    return self.cidades[self.topo]

  def pilhaVazia(self):
    return (self.topo == -1)

  def pilhaCheia(self):
    return (self.topo == self.tamanho - 1)