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
print(f'Gem denne key: {string_key}')

pseudo_data = k.encrypt(raw=bytearray(
    'Hemmelige data æøå # € ¤ z', encoding='UTF8'))
klartekst_data = k.decrypt(enc = pseudo_data)

x = 7