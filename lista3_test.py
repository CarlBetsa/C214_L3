import unittest
from lista3 import ContaPalavras, ObservaPalavras

class ContaPalavrasTest(unittest.TestCase):
    def testa_quantidade_de_palavras(self):
        counter = ContaPalavras()
        observer = ObservaPalavras(counter)
        counter.addObserver(observer)

        frase = "Testando se a contagem de palavras funciona como esperado."
        counter.notificaObservers(frase)

        self.assertEqual(observer.numPalavras, 9)

    def testa_quantidade_de_palavras_par(self):
        counter = ContaPalavras()
        observer = ObservaPalavras(counter)
        counter.addObserver(observer)

        frase = "Contando palavras com número par de caracteres."
        counter.notificaObservers(frase)

        self.assertEqual(observer.numPalavrasPar, 5)

    def testa_palavras_iniciadas_com_maiuscula(self):
        counter = ContaPalavras()
        observer = ObservaPalavras(counter)
        counter.addObserver(observer)

        frase = "CONtando pALAVRAS ComeçadaS COM MaIúScUlAs."
        counter.notificaObservers(frase)

        self.assertEqual(observer.comecaMaiuscula, 4)

    def testa_frase_em_branco(self):
        counter = ContaPalavras()
        observer = ObservaPalavras(counter)
        counter.addObserver(observer)

        frase = ""
        counter.notificaObservers(frase)

        self.assertEqual(observer.numPalavras, 0)
        self.assertEqual(observer.numPalavrasPar, 0)
        self.assertEqual(observer.comecaMaiuscula, 0)

if __name__ == "__main__":
    unittest.main()
