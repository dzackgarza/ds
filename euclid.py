def gcd(a,b):
    """
    Given two digits, compute the greatest common divisor
        using Euclid's algorithm.

    ***  Test Cases     ***
    >>> gcd(42,35)
    7
    >>> gcd(612,1275)
    51
    >>> gcd(49831,825579)
    1
    >>> gcd(75,21)
    3
    >>> gcd((2 ** 2) * 7 * 13, (2 ** 3) * (3 ** 4) * (7 ** 2))
    28
    
    """
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)

def lcm(a,b):
    """
    Given two integers, compute the least common multiple.

    >>> lcm(75,21)
    525
    >>> lcm(52,81)
    4212
    >>> lcm(15,21)
    105
    >>> lcm((2**2)*(7)*(13),(2**3)*(3**4)*(7**2))
    412776
    """
    return (a * b)/gcd(a,b)

def egcd(a,b):
    """
    Use the Extended Euclidean Algorithm to solve equations of the form
        ax + by = gcd(a,b) for (x,y), given (a,b)
    >>> egcd(9,6)
    (1, -1)
    >>> egcd(99,78)
    (-11, 14)
    >>> egcd(65,40)
    (-3, 5)
    >>> egcd(1239,735)
    (-16, 27)
    """
    if(b==0):
        return (1,0)
    else:
        q,r = divmod(a,b)
        s,t = egcd(b,r)
        return (t, s-(q*t)) 

def multinv(m,n):
    """
    Given two integers, return the multiplicative inverse of m mod n
    When a and b are relatively prime, ax + by = 1
        x is then the multiplicative inverse of m mod n
        y is the multiplicative inverse of n mod m
    >>> multinv(6735,1343)
    -470
    """
    x,y = egcd(m,n)
    return x

def decrypt(e):
    """
    Given three numbers, return the corresponding decypted values
    (m*e+k)mod26
    m=5, k=11
    >>> decrypt(16)
    1
    >>> decrypt(7)
    20
    >>> decrypt(5)
    4
    """
    m,k = (5,11)
    return ( multinv(m,26) * (e-k) ) % 26

def linearcipher(string, m, k):
    """
    Given a string to encypt and two coefficients, return the encrypted string.
    Try with m=5, k=11
    
    >>> linearcipher("SECRET", 5, 11)
    'XFVSFC'
    >>> linearcipher("MESSAGES", 5, 11)
    'TFXXLPFX'
    >>> linearcipher("BUFFYSLAYSVAMPRES",5,11)
    'QHKKBXOLBXMLTISFX'
    """
    return decode( [ linear(m, x, k) for x in encode(string) ] )
    
def lineardecipher(message):
    """
    >>> lineardecipher("QHKKBXOLBXMLTISFX")
    'BUFFYSLAYSVAMPRES'
    >>> lineardecipher("LXFVSFCTFXXLPF")
    'ASECRETMESSAGE'
    >>> lineardecipher('QBDAZYXQFLSA')
    'BYODINSBEARD'
    """
    return decode( [ decrypt(x) for x in encode(message) ] )


def coprime(a,b):
    """ Given two integers, return whether or not they are coprime.
    """
    if(gcd(a,b)==1):
        return "Yes"
    else:
        return "No"



def encode(str):
    """
    Given a string of uppercase letters, return a list of numbers
    using the mapping A->0, B->1, C->2, etc.
     
    >>> encode('ABC')
    [0, 1, 2]
    >>> encode('SIERRA')
    [18, 8, 4, 17, 17, 0]
    >>> encode('MATHISCOOL')
    [12, 0, 19, 7, 8, 18, 2, 14, 14, 11]
    """
 
    return [ ord(c) - 65 for c in list(str) ]
        
def decode(lon):
    """
    Given a list of numbers where A=0, B=1, etc.,
    return the corresponding string.
   
    
    >>> decode( [18, 8, 4, 17, 17, 0] )
    'SIERRA'
    >>> decode( [12, 0, 19, 7, 8, 18, 2, 14, 14, 11] )
    'MATHISCOOL'
    """
    return "".join(chr(n + 65) for n in lon)

def shiftcipher(str, k):
    """
    Given a string and k, return the shifted string.
 
    >>> shiftcipher('SIERRA', 15)
    'HXTGGP'
    >>> shiftcipher('MATHISCOOL', 15)
    'BPIWXHRDDA'
    """

    return decode( [ shifter(x, k) for x in encode(str) ] )

def linear (m,a,k):
    """
    Given three numbers, encypt them using the formula (m*a+k) mod 26
    >>> linear(10,12,13)
    3
    >>> linear(13,6,26)
    0
    >>> linear(10,2,5)
    25
    """
    return (m*a+k) % 26

def shifter(n,k):
    """
    Returns the result of the mapping function (n+k) mod 26
    
    >>> shifter(12, 15)
    1
    >>> shifter(18, 13)
    5
    >>> shifter(24, 10)
    8
    """
    
    return (n+k) % 26
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)
