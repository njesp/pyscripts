"""
FSE Pseudonymisering, PoC
"""
import base64
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256


class FSEKryptoDingenot(object):

    def __init__(self):
        self.bs = 32
        self.key = None

    def genkey(self, keystr):
        self.key = SHA256.new(data=keystr.encode()).digest()
        return base64.encodebytes(s=self.key)

    def setkey(self, keystrbase64):
        self.key = base64.decodebytes(s=keystrbase64)

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]


if __name__ == "__main__":
    pass_phrase = """
    Da jeg gik ud over Langebro
    en tidlig mandag morgen
    da så jeg en der stod og græd.
    Hvis du tør - så kom med mig.
    """

    k = FSEKryptoDingenot()

    strk = k.genkey(keystr=pass_phrase)
    # Gem strk, det er den læsevenlige nøgle. Pass frasen skal kun bruges en
    # gang initielt. Jo længere jo bedre. strk er printbar udgave af selve nøglen der er
    # afledt af pass frasen.
    k1 = k.key
    k.setkey(keystrbase64=strk)
    k2 = k.key
    if k1 == k2:
        print('xxx')
