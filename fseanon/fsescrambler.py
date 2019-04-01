"""
Scrambler
"""
import string
from Cryptodome.Random import random
import pyffx


class FseScramble(pyffx.String):
    """
    Scrambler klassen. Laver ikke meget, det meste er delegeret til pyffx.
    """
    def __init__(
            self,
            key,
            length,
            alphabet=string.punctuation + string.ascii_letters + string.digits,
    ):
        super(FseScramble, self).__init__(ffx=key, length=length, alphabet=alphabet)

def genkey(length=64):
    """
    Generer nøgle
    """
    return ''.join(random.choice(string.punctuation +
                                    string.ascii_letters +
                                    string.digits)
                    for _ in range(length))
