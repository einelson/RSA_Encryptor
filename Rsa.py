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
        # convert message to binary
        self.m=self.convert_to_binary(message)
        # print(self.m)

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
        p,q=self.generate_primes()
        n=self.get_modulus(p,q)
        t=self.get_totient(p,q)
        e=self.get_encryption_exponent(t)
        d=self.get_decryption_exponent(t,e)
        # return encrypted message
        return self.get_ciphertext(e,n),n,d

    # message decryptor
    def decrypt(self, cypher_text,n,d):
        decrypted_message=list()
        for c in cypher_text:
            decrypted_message.append(str((c^d)%n))
        # convery binary to string of letters
        return ''.join([chr(int(x, 2)) for x in decrypted_message])

    # gets p and q, the primes
    def generate_primes(self):
        p=self.get_p()
        q=self.get_q(p)
        return p,q

    # generate random large prime
    def get_p(self):
        return number.getPrime(100)

    # generate another large prime different than p but with same number of digits
    def get_q(self,p):
        q= number.getPrime(100)
        # make sure that p and q are the same length and not the same number number
        while len(str(q))!=len(str(p)) or q==p:
            q= number.getPrime(100)
        return q

    # gets the modulus
    def get_modulus(self,p,q):
        n=p*q
        # sheck to make sure the modulus is larger than the message
        # if len(n) < len(self.m):
        #     self.generate_primes()
        #     n=self.p*self.q
        return n
        
    # gets the totient
    def get_totient(self,p,q):
        t=(p-1)*(q-1)
        return t

    def get_encryption_exponent(self,t):
        # coprime to t
        return 65537

    def get_decryption_exponent(self,t,e):
        # inverse of e %t
        # return (e^(-1))%t
        return e%t

    def get_ciphertext(self,e,n):
        cypher_list=list()
        for x in self.m:
            cypher_list.append((int(x)^(e))%n)
        return cypher_list


# RSA a message
x=RSA(message="Hello World")
encrypted_message,n,d=x.encrypt()
print('Encrypted Message:')
print(encrypted_message)
decrypted_message=x.decrypt(encrypted_message,n,d)
print('Decrypted Message:')
print(decrypted_message)