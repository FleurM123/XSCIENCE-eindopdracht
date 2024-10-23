import re 
import time
import random
import json
import urllib.request

def mcdonalds_happymeal_jewerly():
  url = 'https://fakestoreapi.com/products/category/jewelery'
  response = urllib.request.urlopen(url)
  result = json.loads(response.read())
  
  result = result[0]
  print(result)
  happymeal_jewerly= result["title"]


mcdonalds_happymeal_jewerly()


patronen = { 
   "Ik heb een vraag over (.*)":"MCDEWERKER: Oke!, je hebt een vraag over {}", 
   "Ik vind de McDonalds(.*)":"MCDEWERKER: Dus je vind de McDonalds {}?",
   "Ik heb een klacht over(.*)":"MCDEWERKER: Je hebt dus een klacht over {}?",
   "Ik vind het eten(.*)":"MCDEWERKER: Dus je vind het eten {}?",
   "Het ruikt hier naar (.*)":"MCDEWERKER: Ja? Ik ruik niet echt de geur van {}",
   "Jullie maken alles te (.*)":"MCDEWERKER: Oh echt? Dat is dan alleen uw mening, ik vind het niet zo {}",
   "Ik weet niet of ik hier nog eens kom, mijn ervaring was redelijk (.*)":"MCDEWERKER: Oh, oke, bedankt voor het komen, al was het {}"

}


antwoorden = {
  "Hallo": ["MCDEWERKER: Hallo, waarvoor komt u?", "MCDEWERKER: Hoi!, hoe gaat het?", "MCDEWERKER: Hallo, hoe kan ik je helpen?"],
  "Hey, mag ik gratis eten?": ["MCDEWERKER: NEE! Waarom zou dat wel mogen?", "MCDEWERKER: Nee sorry, gewoon betalen!", "MCDEWERKER: Nope! Absoluut niet! Betalen! En achteraan sluiten, ik zag u de rij skippen!"],
  "Hoe gaat het?": ["MCDEWERKER: Het gaat goed, bedankt!", "MCDEWERKER: Het gaat prima, met jou?", "MCDEWERKER: Goed hoor"],
  "*Skipt de rij*": ["MCDEWERKER: Dat zag ik!", "MCDEWERKER: NU ACHTERAAN SLUITEN!", "MCDEWERKER: U moet even in de rij gaan staan, iedereen wacht al erg lang, dus u moet dat ook!"],
  "Het gaat goed": ["MCDWERKER: Fijn om te horen!", "MCDEWERKER: Gelukkig maar, een goed humeur voor een heerlijke portie McDonald's!", "MCDEWERKER: Wat goed, dan zal je wel een nog grotere glimlach krijgen van een hapje McDonald's!"],
  "Het gaat slecht": ["MCDEWERKER: Wat vervelend, kan ik je opvrolijken met een paar gratis extraatjes?", "MCDEWERKER: Oh, nou geen zorgen, ons eten smaakt heerlijk, binnen no time staat er weer een mooie lach op je gezicht geplakt."],
  "Wat is er?": ["MCDEWERKER: Er is niks", "MCDEWERKER: Het is niks ergs", "MCDEWERKER: Niks eigenlijk"],
  "Waarom duurt het zo lang?": ["MCDEWERKER: Bent u zo ongeduldig? Even rustig aan hoor!", "MCDEWERKER: Omdat u heel veel besteld hebt en wij ook andere klanten moeten bedienen.", "Omdat u ongeduldig bent en wij dit moeten maken en dat tering veel moeite kost."],
  "Ik heb een vraag": ["MCDEWERKER: Ik ben benieuwd, wat is je vraag?", "MCDEWERKER: Wat is je vraag?", "MCDEWERKER: Vertel, ik zal het zo goed mogelijk proberen te beantwoorden"],
  "Waarom duurt het zo lang voordat ik mijn ijsje krijg?": ["MCDEWERKER: De ijsmachine wordt nu gerepareerd, hij is een eeuw kapot geweest", "MCDEWERKER: Dat kan u niet besteld hebben, de machine is stuk", "Wees geduldig beste klant, we doen ons best, u hoeft nog maar drieduizend jaar te wachten, dan is de ijsmachine weer gerepareerd."],
  "Ik ben zo boos! Jullie moeten sluiten! Nu meteen!": ["MCDEWERKER: Oh nee he, niet weer zo'n karen...", "MCDEWERKER: Wat is er mis?", "MCDEWERKER: Vertel eens, waarom uit u ineens zo'n haat naar ons?"],
  "Mijn kind had hier kipnuggets vandaan gehaald en toen m'n lieve kindje die gisteren at werd het arme kind ziek! Hier is het bonnetje voor bewijs!": ["MCDEWERKER: Daar kunnen wij echt niets aan doen, kijk goed, die kipnuggets zijn van vijf jaar geleden.", "MCDEWERKER: Oke, dit kan me niks schelen, veel plezier met een ziek kind en verbannen zijn uit de McDonald's.", "MCDEWERKER: Nou hier zijn wat medicijnen, hopelijk wordt uw kind beter."],
  "Ik heb een klacht!": ["MCDEWERKER: Wat is uw klacht?", "MCDEWERKER: Nee, u hebt geen klacht maar u hebt wel toestemming om uit te glijden en in de modder te vallen."],
  "Ik haat jullie!": ["MCDEWERKER: Dat kan ons niks schelen, u bent toch lelijk.", "MCDEWERKER: BOEIE! Als u niet meer komt hoeven wij uw oorverdovende piepstem niet meer te horen, u lijkt wel een krijsende baby"],
  "Doe eens even normaal": ["MCDEWERKER: Het spijt me, ik moet inderdaad even normaal doen.", "MCDEWERKER: Oke, ik ga normaal doen.", "MCDEWERKER: Prima, ik doe normaal!!!!!"],
  
}


def krijg_antwoord(vraag): 
  if vraag in antwoorden: 
      time.sleep(random.randint(1, 3))
      return antwoorden[vraag] 
  else: 
      time.sleep(random.randint(1, 3))
      return "IK hoor je, je zei: " + vraag 



def krijg_antwoord_patroon(bericht):
   
    time.sleep(random.randint(1, 3))
    for patroon in patronen: 
        match = re.search(patroon,bericht) 
        if match: 
            return patronen[patroon].format(match.group(1))
    
    if bericht in antwoorden: 
        return random.choice(antwoorden[bericht])
    else: 
        return "MCDEWERKER: Ik hoor je, je zei: " + bericht 
  
[{"id":5,"title":"John Hardy Women's Legends Naga Gold & Silver Dragon Station Chain Bracelet","price":695,"description":"From our Legends Collection, the Naga was inspired by the mythical water dragon that protects the ocean's pearl. Wear facing inward to be bestowed with love and abundance, or outward for protection.","category":"jewelery","image":"https://fakestoreapi.com/img/71pWzhdJNwL._AC_UL640_QL65_ML3_.jpg","rating":{"rate":4.6,"count":400}},{"id":6,"title":"Solid Gold Petite Micropave ","price":168,"description":"Satisfaction Guaranteed. Return or exchange any order within 30 days.Designed and sold by Hafeez Center in the United States. Satisfaction Guaranteed. Return or exchange any order within 30 days.","category":"jewelery","image":"https://fakestoreapi.com/img/61sbMiUnoGL._AC_UL640_QL65_ML3_.jpg","rating":{"rate":3.9,"count":70}},{"id":7,"title":"White Gold Plated Princess","price":9.99,"description":"Classic Created Wedding Engagement Solitaire Diamond Promise Ring for Her. Gifts to spoil your love more for Engagement, Wedding, Anniversary, Valentine's Day...","category":"jewelery","image":"https://fakestoreapi.com/img/71YAIFU48IL._AC_UL640_QL65_ML3_.jpg","rating":{"rate":3,"count":400}},{"id":8,"title":"Pierced Owl Rose Gold Plated Stainless Steel Double","price":10.99,"description":"Rose Gold Plated Double Flared Tunnel Plug Earrings. Made of 316L Stainless Steel","category":"jewelery","image":"https://fakestoreapi.com/img/51UDEzMJVpL._AC_UL640_QL65_ML3_.jpg","rating":{"rate":1.9,"count":100}}]
      
while True:
  bericht = input("YOU: ")
  antwoord = krijg_antwoord_patroon(bericht)
  print("Bot: " + antwoord)