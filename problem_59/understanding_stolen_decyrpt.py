
an_s = [79,59,12,2,79,35,8,28,20,2,3,6]


def decrypt(s, t):
    """
    This function will take a ascii value and
    a string(the key) and xor with the encrypted text
    and find the real solution
    """
    return ''.join(chr(a ^ ord(b)) for a, b in zip(s, t))