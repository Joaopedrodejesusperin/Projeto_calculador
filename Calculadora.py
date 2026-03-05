class Calculadora:
    
    def Menu(self):
        print("Selecione a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        

    def soma(self, a, b):
        return a + b
    
    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b
    
    def divisao(self, a, b):
        if b == 0 or a == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return a / b
    