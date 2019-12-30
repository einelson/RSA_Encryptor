###########################
# RSA Encryptor/Decryptor #
###########################

#############
# Libraries #
#############
# for generating primes
from Crypto.Util import number

#############
# Class RSA #
#############
class RSA:
    # initalize
    def __init__(self,message):
        self.m=message

    # messaege encryptor
    def encrypt(self):
        # for now
        self.generate_primes()
        self.get_modulus()
        print(self.p)
        print(self.q)
        print(self.n)
        return 0

    # message decryptor
    def decrypt(self):
        return 1

    # gets p and q, the primes
    def generate_primes(self):
        self.get_p()
        self.get_q()

    # generate random large prime
    def get_p(self):
        self.p= number.getPrime(100)

    # generate another large prime different than p but with same number of digits
    def get_q(self):
        q= number.getPrime(100)
        # make sure that p and q arent the same length or number
        while len(q)!=len(self.p) or q==self.p:
            q= number.getPrime(100)
        self.q=q

    # gets the modulus
    def get_modulus(self):
        n=self.p*self.q
        # sheck to make sure the modulus is larger than the message
        if len(n) < len(self.m):
            self.generate_primes()
            n=self.p*self.q
        self.n=n

x=RSA(message=9)
# x.generate_primes()
