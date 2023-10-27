'''
RSA - Challenge 39 Cryptopals
Cifracao: calcular c = m**e mod n
Decifração: calcular d = c**d mod n
Consistência: c**d = m**(e.d) = m mod n
Fatorar n em p e q é difícil
'''
import random
import math
import sys


def randomPrime(n):
  return n

def invMod(a, b): 
    an, bn = a, b
    a, b = 1, 0
    while bn > 0:
        q=divmod(an, bn)[0]
        a, b = b, a - b*q
        an, bn = bn, an - bn*q
    while a<0:
        a = a + b
    return a

class RSA:
  def __init__(self):
    # e é o atributo público (3 por conta do desafio)
    self.e = 3
    # Gerar dois números primos grandes (entre 512 e 4096 bits)
    p = 7449161641746400688725134304502546097756840069109838273973265698822203490117233941016722994940857962398457420479437834946570026030291892336736957163630417
    q = 7670420829202182258186219578833221099867335042396299114311188317498872136804394397497199356772521136865013952112194242383782180564960906329338189334571743
    # Atribui p*q à n
    self.n = p*q
    # phi: o(n) = (p - 1).(q - 1)
    o = (p-1)*(q-1)
    # d é o atributo privado e d = e**(-1) mod o
    self._d = invMod(self.e, o)
  
  def cifracao(self, dados):
    # Precisa transformar os dados em inteiro
    dadosCif = int.from_bytes(dados, byteorder='big')
    #Cifracao: calcular c = m**e mod n
    return pow(dadosCif, self.e, self.n)
  
  def decifracao(self, dados):
    #Decifração: calcular d = c**d mod n
    dadosDes = pow(dados, self._d, self.n)
    # Retorna à bytes
    return dadosDes.to_bytes((dadosDes.bit_length() + 7) // 8, 'big')

def main():
    rsa = RSA()
    some_text = b"Alguns veem pinguins, eu so vejo a luz no fim do tunel"
    assert rsa.decifracao(rsa.cifracao(some_text)) == some_text

if __name__ == '__main__':
    main()
