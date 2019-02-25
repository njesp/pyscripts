"""
FSE Pseudonymisering, PoC
"""
import base64
import unittest
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

# pip install pycryptodome


class FSEKryptoDingenot(object):

    def __init__(self):
        self.bs = 32
        self.key = None
        self.iv = None

    def genkey(self, keystr):
        self.key = SHA256.new(data=keystr.encode()).digest()
        self.iv = self.key
        return base64.encodebytes(s=self.key)

    def setkey(self, keystrbase64):
        self.key = base64.decodebytes(s=keystrbase64)
        self.iv = self.key

    def encrypt(self, raw):
        raw = self._pad(raw)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return base64.b64encode(cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]


class TestFSEKrypto(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == "__main__":
    unittest.main()

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
    assert (k.key is not None), "Key must be set"
    k.setkey(keystrbase64=strk)
    k2 = k.key
    if k1 == k2:
        print('xxx')
