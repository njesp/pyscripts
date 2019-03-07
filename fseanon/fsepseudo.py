"""
Pseydonymization PoC
"""
import base64
import unittest
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Cipher import RC4
# pip install pycryptodome


class FSEKryptoDingenot(object):

    def __init__(self):
        """
        Simple constructor. Bs is blocksize used for padding. 
        AES-256-CBC requires padding to a multipla of blocksize. 
        """
        self.bs = AES.block_size
        self.key = None
        self.iv = None

    def genkey(self, keyphrasestr):
        """
        Generate 256 bit key from (preferabley) long passphrase
        Return a base64 coded representation of key for future 
        psudonymizations with same key or un-pseudonymization.
        IV set to the firs 128 bit of the key, so pseudonimizations
        will be deterministic. This is known bad-crypto, but 
        a neccessary property of pseudonymization.
        """
        self.key = SHA256.new(data=keyphrasestr.encode()).digest()
        self.iv = self.key[0:AES.block_size]
        return base64.encodebytes(s=self.key)

    def setkey(self, keystrbase64):
        """
        Set key from base64 encoded key, previously generated.
        """
        self.key = base64.decodebytes(s=keystrbase64)
        self.iv = self.key[0:AES.block_size]

    def encrypt(self, raw):
        raw = self._pad(raw)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return base64.b64encode(cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return self._unpad(cipher.decrypt(enc)).decode('utf-8')

    def _pad(self, s):
        """
        Pad data to next multipla of 16 bytes (AES blocksize) with identical low ascii character bytes.
        Padding will always take place, even if data is multipla of AES.block_size (16) bytes. 
        Then another 16 bytes will be added. 
        """
        return s + (self.bs - len(s) % self.bs) * bytes(self.bs - len(s) % self.bs)

    def _unpad(self, s):
        """
        Cut padding from decrypted data. A tail of last byte is known to be padding. 
        """
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
