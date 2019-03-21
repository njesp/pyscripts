import string
import pyffx

class FseScramble(pyffx.String):
    def __init__(
        self,
        key,
        length,
        alphabet=string.punctuation + string.ascii_letters + string.digits,
    ):
        super(FseScramble, self).__init__(ffx=key, length=length, alphabet=alphabet)
