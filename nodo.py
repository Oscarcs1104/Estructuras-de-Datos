class nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    def devolver_valor(self):
        print(self.valor)

    def asignar_siguiente(self, nodo):
        self.siguiente = nodo

    def cambiar_valor(self,valor):
        self.valor = valor


Nodo1 = nodo("a")

Nodo2 = nodo("b")

print(Nodo2)
nodo.devolver_valor(Nodo1)

Nodo1.cambiar_valor("z")

nodo.devolver_valor(Nodo1)

Nodo1.asignar_siguiente(Nodo2)

print(Nodo1.siguiente)
