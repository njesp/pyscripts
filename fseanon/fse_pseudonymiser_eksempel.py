"""
FSE Pseudonymisering, Eksempel på brugC
"""
import fsepseudo as fp

pass_phrase = """
Når jeg sjasker gennem byen
med en kaktus i min hånd
og regnen drypper ned på min næse
er det som et perspektiv.
Næ, jeg har hånden fuld
jeg har hånden fuld af liv
og så med et der stråler solen
ja og alting drejer rundt. """

k = fp.FSEKryptoDingenot()
string_key = k.genkey(keyphrasestr=pass_phrase)
# Gem string_key, det er den læsevenlige nøgle. 
k1 = k.key
assert (k.key is not None), "Key must be set"
k.setkey(keystrbase64=strk)
k2 = k.key
if k1 == k2:
    print('xxx')
