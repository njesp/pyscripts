Tanker bag:
Reversibel og deterministisk pseudonymisering af nøglefelter bestående af tekst. 
Output skal gerne ikke være meget anderledes i længde og type.

Involverede algoritmer og implementeringer skal være langtidsholdbare. Selv efter lang tid skal man kunne
genidentificere data. 

Anonymiseringen skal være unik for hvert projekt. Dette styres ved at der ved projektstart genereres en sikker 
projekstspecifik nøgle af god kryptografisk kvalitet længde og randomness.




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
