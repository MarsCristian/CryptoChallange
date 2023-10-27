import random
from Crypto.Util import number


class RSA:


    #Generate 2 random primes. 
    #We'll use small numbers to start, so you can just pick them out of a prime table. 
    #Call them "p" and "q"
    def GenerateRandomPrimeNumber(self):
        primo = number.getPrime(1024)
        return primo
    
    def Egcd(self):
        #TODO implementa o bgl ai
        return 'kkkkkkk n ta implementado'

    def Invmod(self):
        #TODO implementa o invmod
        return 'kkkkkkk n ta implementado'
    

    def GenerateRSA(self):
        p = self.GenerateRandomPrimeNumber()
        q = self.GenerateRandomPrimeNumber()

        n = p*q

        totient = (p-1)*(q-1)

        pass


