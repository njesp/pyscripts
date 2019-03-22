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
# Det er muligvis bedre at eksponere alphabetet til brugeren, så hvis man er sikker på 
# kun cifre, så kan outputtet også være kun cifre. 
# Det er en beslutning der skal træffes up front for hver ny kryptering
# Hvis der dukker nye tegn op efterfølgende er det ikke godt.

# Gendata. Krypter .fam. Omsorter. Følg https://www.biostars.org/p/103945/
# 

#k = ''.join(random.choice(string.punctuation + string.ascii_letters + string.digits) for _ in range(64))
#
#print("key: " + k)
#
# Initier scrambler
#
#e = fs.FseScramble(key=k.encode(), length=10)