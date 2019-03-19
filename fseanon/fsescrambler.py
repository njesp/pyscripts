import string
import pyffx


class FseScramble(pyffx.String):
    def __init__(self, key, length, alphabet=string.punctuation + string.ascii_letters + string.digits):
        super(FseScramble, self).__init__(ffx=key, length=length, alphabet=alphabet)


e = FseScramble(key=b'02sxdssxxxxxxxxfkkallxcffssdfg', length=6)
print(e.encrypt('abcde'))
print(e.decrypt('acbacc'))
