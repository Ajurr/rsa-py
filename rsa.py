import random

#primality test to ensure p and q are prime numbers
def prime(a):
    if a < 2: return False
    for x in range(2, int(a ** 0.5) + 1):
        if a % x == 0:
            return False
    return True

#euclidean algorithm for ensuring corpimality
def computeGCD(x, y):
    while(y):
       x, y = y, x % y
    return abs(x)

#extended euclidean algorithm for getting inverse of e for d
def exteuclid(a, b):
    r1 = a
    r2 = b
    s1 = int(1)
    s2 = int(0)
    t1 = int(0)
    t2 = int(1)
     
    while r2 > 0:
         
        q = r1//r2
        r = r1-q * r2
        r1 = r2
        r2 = r
        s = s1-q * s2
        s1 = s2
        s2 = s
        t = t1-q * t2
        t1 = t2
        t2 = t
         
    if t1 < 0:
        t1 = t1 % a
         
    return (r1, t1)

#encryption method
def encryption(p, q, m):
    
    #primality testing of p and q
    while True:
        if(prime(p) == False):
            p = int(input(str(p) + ' is not prime, please input a prime number: '))
        elif(prime(q) == False):
            q = int(input(str(q) + ' is not prime, please input a prime number: '))
        else:
            break

    n = p * q #product of 2 primes = n
    p1q1 = (p-1)*(q-1) #calculating (p-1)(q-1)
    c = [] #initialize encrypted message

    #loop for randomly selecting e between 1 and 100, 1 and 100 is arbitrary, just for example
    while True:
        e = random.randint(1, 100)
        if computeGCD(p1q1, e) == 1:
            break
    
    #extended euclidean algorithm called to get multiplicative inverse of e using p1q1
    r, d = exteuclid(p1q1, e)

    #ensuring message may be decrypted
    if r == 1:
        d = int(d)
        print("decryption key is: ", d)
    else:
        print("Multiplicative inverse for the given encryption key does not exist. Choose a different encryption key ")
    
    #publish the encryption key and product of 2 primes n
    print("encryption key e: "+ str(e) + "\n" + "product of two primes n: " + str(n)) 

    k = random.randint(1, 10) #random number of chunks to split into, 1-10 is arbitrary for examples
    chunkLength = len(str(m)) // k #calculating chunk length here

    #separating message into chunks
    mChunked = []
    for idx in range(0, len(str(m)), chunkLength):
        mChunked.append(str(m)[idx : idx + chunkLength])
    for i in mChunked:
        c.append(int(i) ** e % n)
    print("encrypted message: " + str(c))
    return c, d, n

#decryption method applies multiplicative inverse of e calculated earlier to reverse the encryption method transform back to the original message
def decryption(c, d, n):
    m = []
    for i in c:
        m.append(int(i)**d % n)
    print("decrypted message: "+ str(m))

if __name__ == '__main__':
    c, d, n = encryption(int(input("p: ")), int(input("q: ")), int(input("message: ")))
    decryption(c, d, n)