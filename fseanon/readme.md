Tanker bag:
Reversibel pseudonymisering af alfanumeriske nøglefelter. 
Output printbart 
Input tages som strøm af bytes. Dette gælder begge veje, 
så hvis man kan antage en UTF8 kodning på input, så gælder dette også efter.
Ligeså ASCII, eller for så vidt også et vilkårligt bitmønster. 
Man skal gerne huske, hvilken encoding data kommer fra. 
input(encoding_x) -> crypt -> kryptotekst(ascii/base64) -> dekrypt -> input(encoding_x).
Reelt er dette nok ikke et problem, et sæt erfarne øjne kan formentlig hurtigt afgøre det. 

Princippet er at anvende gængse algoritmer, så der kan genimplementeres 
også langt ude i fremtiden. Ikke bare gængse algoritmer, men gerne nogle 
med en del år på bagen og multiple robuste implementeringer. 

Dette for at sikre langtidsholdbarhed. 

Derudover er det vigtigt at vælge en stærk kryptering. 

Forslag: Kryptering af input cleartext med AES-256. ciphertext base64-encodes for at sikre 
at det krypterede et til at håndtere (synlige tegn uanset tegnsæt i klientsoftware).

Ciphertext får en længde der svarer til input rundet op til nærmeste multipla af 16 bytes 
og tillagt 33% (som følge af base64). 10 bytes input bliver til 22 bytes (16 + 33%).

Med nogenlunde korte nøglelængder er dette ikke et stort problem. 

AES256 spiser måske nok en smule CPU, men det er formentlig ikke et reelt problem. 
Så tit foregår det heller ikke. 

Efterfølgende sortering. Eftersom der fremover formentlig en gang imellem vil komme datasæt med 
rigtig-rigtig mange rækker foreslås en alternativ slutsortering, idet
rækkerne sorteres efter en genereret temporær nøgle i fx 10 millioner batches. 
Enhver række vil så havne i samme 10 millioners segment af fx 100 milliarder rækker. 
Ikke sikkerhedsmæssigt noget problem, men det gør sorteringen gennemførlig. 

Krypteringsnøgler. 

AES-256 bruger en 256-bit værdi som nøgle (surprise). Denne nøgle skal bare være så 
tilfældig som muligt. I praksis er det en god ide at bruge relativt lange tekster 
(Brudstykker fra Gasolins The Black Box, fx) og lade denne tekst komme en tur gennem SHA-512/256
og bruge hash-værdien som nøgle. Det kan overvejes om man bare skal gemme selve nøglen og 
glemme den den lange tekst (som har gjort sin gavn).

IV skal være ens for samme nøgle => deterministisk kryptering.
