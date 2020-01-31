###########################
# RSA Encryptor/Decryptor #
###########################

#############
# Libraries #
#############
# for generating primes
from Crypto.Util import number
from sympy import isprime

#############
# Class RSA #
#############
class RSA:
    # initalize
    def __init__(self,message):

        self.m=self.convert_to_binary(message)

    # converts message to numberical form
    def convert_to_binary(self, message):
        # change message into binary
        binary =' '.join(format(ord(x), 'b') for x in message)
        # each letter is in a list
        binary=binary.split(' ')
        return binary


    # messaege encryptor
    def encrypt(self):
        # for now
        self.generate_primes()
        self.get_modulus()
        self.get_totient()
        self.get_encryption_exponent()
        self.get_ciphertext()
        # print("message(m):" + str(self.m))
        print("large prime(p):" + str(self.p))
        print("another large prime(q):" + str(self.q))
        print("modulus(n):" + str(self.n))
        print("totient(t):" + str(self.t))
        print("encryption exponent(e):" + str(self.e))
        print("ciphertext(c):" + str(self.c))


    # message decryptor
    def decrypt(self):
        print("here")

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
        # make sure that p and q are the same length and not the same number number
        while len(str(q))!=len(str(self.p)) or q==self.p:
            q= number.getPrime(100)
        self.q=q

    # gets the modulus
    def get_modulus(self):
        n=self.p*self.q
        # sheck to make sure the modulus is larger than the message
        # if len(n) < len(self.m):
        #     self.generate_primes()
        #     n=self.p*self.q
        self.n=n
        
    # gets the totient
    def get_totient(self):
        t=(self.p-1)*(self.q-1)
        self.t=t

    def get_encryption_exponent(self):
        # coprime to t
        # use isprime function. this will probably be inefficient for now
        e=self.t
        e=e-1
        while(isprime(e)!= True):
            e=e-1
        self.e=e

    def get_ciphertext(self):
        self.c=((self.m)^(self.e))%self.n

# RSA a message
x=RSA(message="Hello World")
# x.encrypt()
