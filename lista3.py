class ContaPalavras:
    def __init__(self):
        self.palavras = []

    def addObserver(self, observer):
        self.palavras.append(observer)

    def notificaObservers(self, frase):
        for observer in self.palavras:
            observer.attObserver(frase)

class ObservaPalavras:
    def __init__(self, contador):
        self.contador = contador
        self.numPalavras = 0
        self.numPalavrasPar = 0
        self.comecaMaiuscula = 0

    def attObserver(self, frase):
        fraseFinal = ''.join(char for char in frase if char.isalpha() or char.isspace())

        palavras = fraseFinal.split()
        self.numPalavras = len(palavras)
        self.numPalavrasPar = sum(1 for word in palavras if len(word) % 2 == 0)
        self.comecaMaiuscula = sum(1 for word in palavras if word[0].isupper())

    def mostraInfo(self):
        print("Numero de palavras:", self.numPalavras)
        print("Numero de palavras com quantidade par de caracteres:", self.numPalavrasPar)
        print("Numero de palavras começadas com maiúsculas:", self.comecaMaiuscula)

def main():
    contador = ContaPalavras()
    observer = ObservaPalavras(contador)
    contador.addObserver(observer)

    frase = input("Digite uma frase: ")
    contador.notificaObservers(frase)
    observer.mostraInfo()

if __name__ == "__main__":
    main()
