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
        """
        Simple constructor. Bs is blocksize used for padding. 
        AES-256-CBC requires padding to a multipla of blocksize. 
        """
        self.bs = 32
        self.key = None
        self.iv = None

    def genkey(self, keyphrasestr):
        """
        Generate 256 bit key from (preferabley) long passphrase
        Return a base64 coded representation of key for future 
        psudonymizations with same key or un-pseudonymization.
        Key and IV set to the same, so future pseudonimizations
        will give same result. 
        """
        self.key = SHA256.new(data=keyphrasestr.encode()).digest()
        self.iv = self.key
        return base64.encodebytes(s=self.key)

    def setkey(self, keystrbase64):
        """
        Set key from base64 encoded key, previously generated.
        """
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

    def test_key_is_generated(self):
        k = FSEKryptoDingenot()
        strk = k.genkey(keyphrasestr="Goddag mand økseskaft")
        k1 = k.key
        self.assertIsNotNone(k.key, "Key must be set")

    def test_key_is_same_generated_or_set(self):
        k = FSEKryptoDingenot()
        strk = k.genkey(keyphrasestr="Goddag mand økseskaft")
        k1 = k.key
        k.setkey(keystrbase64=strk)
        k2 = k.key
        self.assertEqual(
            k1, k2, "Key skal være det samme, genereret eller sat")

if __name__ == "__main__":
    unittest.main()
