def quad(x):
    """
    Given a number, return it raised to the 4th power.
 
    >>> quad(2)
    16
    >>> quad(1)
    1
    """
 
    return x ** 4

def triarea(base, height):
    """
    Given the base and height of a triangle, return its area.
    
    >>> triarea(3,4)
    6
    >>> triarea(3,3)
    4
    >>> triarea(100,5)
    250
    """
 
    return base * height / 2
 
def fullname(fname, lname):
    """
    Given a first name and a last name, return the full name in
    the format "lastname, firstname"
 
    >>> fullname("Michael", "Jackson")
    'Jackson, Michael'
    """
 
    return lname + ", " + fname
    
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

def linearcipher(string, m, k):
    """
    Given a string to encypt and two coefficients, return the encrypted string.
    Try with m=5, k=11
    
    >>> linearcipher("SECRET", 5, 11)
    'XFVSFC'
    >>> linearcipher("MESSAGES", 5, 11)
    'TFXXLPFX'
    
    """
    return decode( [ linear(m, x, k) for x in encode(string) ] )

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)
