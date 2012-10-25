import random

""" Given a string, return a list of numbers (ASCII values). """
def encode(s):
    """
    >>> encode('discrete')
    [100, 105, 115, 99, 114, 101, 116, 101]
    >>> encode('abc')
    [97, 98, 99]
    >>> encode('zyx')
    [122, 121, 120]
    """
    return [ord(c) for c in list(s)]


"""Given a list of numeric ASCII values, return the corresponding string."""
def decode(ascii):
    """
    >>> decode([97, 98, 99])
    'abc'
    >>> decode([100, 105, 115, 99, 114, 101, 116, 101])
    'discrete'
    >>> decode([122, 121, 120])
    'zyx'
    """
    return "".join(chr(a) for a in ascii)


""" Given the encyption exponent e, the modulus n, and a message m, encypt the message."""
def encrypt(e, n, m):
    """
    >>> encrypt(2,13,9)
    3
    >>> encrypt(44,99,78)
    45
    >>> encrypt(17,377,102)
    163
    >>> 
    """
    return int((m**e)  % n)


"""    Given e, n (the modulus), and a string, encrypt each character
        in the string and return a list of encrypted values. """
def encryptstr(e, n, plain_text_string):
    """
    >>> encryptstr(17, 377, 'discrete')
    [341, 287, 202, 99, 95, 69, 116, 69]
   >>> encryptstr(10,257,'secret')
    [141, 232, 70, 211, 232, 117]
    >>> encryptstr(10,257,'secret')
    [141, 232, 70, 211, 232, 117]
    """
    if (n < 256):
        return "Error: N must be above 256"
    else:
        return  [ encrypt(e,n,x) for x in encode(plain_text_string) ]
    
""" Assuming d and n have already been selected, return the decypted value. """
def decrypt(d, n, c):
    """
    >>> decrypt(257, 377, 341)
    100
    """
    return int(c**d % n)

""" Assuming d and n have already been chosen, return a decrypted list of numbers."""
def decryptstr(d, n, encrypted_list):
    """
    >>> decryptstr(257, 377, [341, 287, 202, 99, 95, 69, 116, 69])
    'discrete'
    """
    return decode( (decrypt(d,n,x) for x in encrypted_list ) )


""" Return the greatest common divisor of two integers """
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

""" Given a p and a q, return the totient (phi) """
def get_totient(p, q):
    return (p-1) * (q-1)

""" Given p and q (which are coprime), compute all possible values of e"""
def liste(p, q):
    """
    >>> liste(5, 11)
    [3, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39]
    """
    n = p*q
    phi = get_totient(p,q)
    return [x for x in range(phi) if  are_coprime(x,phi) and x != 1]

"""
Given a p and a q, return a random value for e
Note: p*q must be larger than the message to be encrypted
"""
def finde(p,q):
    """ >>> finde(5, 11) in liste(5, 11)
    True
    """ 
    n = p*q
    phi = get_totient(p,q)
    
    """ Narrow down the possibilities """
    possible_choices = {x for x in range (phi)}
    possible_choices -= {0,1}
    possible_choices -= {x for x in possible_choices if are_coprime(x,phi) == False}
    
    choice = random.sample (possible_choices, 1)
    """     First argument:          Set to use
             Second argument:    Number to sample
    """
    return int(choice[0])


""" Calculate x and y using the Extended Euclidean Algorithm. """
def egcd(a, b):
    """
    >>> egcd(7, 21)
    (1, 0)
    >>> egcd(13, 40)
    (-3, 1)
    """
    if b == 0:
        return (1, 0)
    else:
        (q, r) = divmod(a, b)
        (s, t) = egcd(b, r)
    return (t, s - q * t)

""" Given two integers, return whether or not they are coprime. """
def are_coprime(a,b):

    if(gcd(a,b)==1):
        return True
    else:
        return False
    
"""Given e and a totient t, return d, the decryption exponent.
    d is the multiplicative inverse of e; that is, it satisfies the equation d*e mod phi = 1
"""
def  find_d(e,p,q):
    """
    >>> find_d(13, 5, 11)
    37
    >>> find_d(17, 29, 13)
    257
    """
    phi = get_totient(p,q)
    d = egcd(e,phi)[0]
    if (d>0):
        return d
    else:
        return d + phi

""" Given an initial p and q, generate a tuple containing the information needed for public/private keys """
def genkeys(p,q):
    """
    >>> (e,d,n) = genkeys(13, 17)
    >>> find_d(e,13,17) == d
    True
    >>> e in liste(13,17)
    True
    """
    e = finde(p,q)
    d = find_d(e, p, q)
    n = get_totient(p,q)
    return (e,d,n)
    
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)
