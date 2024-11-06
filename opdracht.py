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

  happymeal_jewerly= result["title"]
  return happymeal_jewerly




patterns = { 
   "Ik heb een vraag over (.*).":"MCDEWERKER: Oke!, je hebt een vraag over {}", 
   "Ik vind de McDonalds(.*)!":"MCDEWERKER: Dus je vind de McDonalds {}?",
   "Ik heb een klacht over(.*)!":"MCDEWERKER: Je hebt dus een klacht over {}?",
   "Ik vind het eten(.*)!":"MCDEWERKER: Dus je vind het eten {}?",
   "Het ruikt hier naar (.*)!":"MCDEWERKER: Ja? Ik ruik niet echt de geur van {}",
   "Jullie maken alles te (.*)!":"MCDEWERKER: Oh echt? Dat is dan alleen uw mening, ik vind het niet zo {}",
   "Ik weet niet of ik hier nog eens kom, mijn ervaring was redelijk (.*).":"MCDEWERKER: Oh, oke, bedankt voor het komen, al was het {}",
   "Dit bedrijf is erg (.*)!":"MCDEWERKER: Vindt u ons bedrijf echt zo {}?",
   "Ik haat deze plek want (.*)!":"MCDEWERKER: Alleen omdat {}?!",
   "Gekke vraag maar hebben jullie (.*)?":"MCDEWERKER: Nee natuurlijk hebben wij geen {}",
   "Ik wil nu meteen gratis (.*)!":"MCDEWERKER: Het spijt me, u kan niet zomaar binnenstormen en gratis {} eisen"

}


answers = {
  "Hallo": ["MCDEWERKER: Hallo, waarvoor komt u?", "MCDEWERKER: Hoi!, hoe gaat het?", "MCDEWERKER: Hallo, hoe kan ik je helpen?"],
  "Hey, mag ik gratis eten?": ["MCDEWERKER: NEE! Waarom zou dat wel mogen?", "MCDEWERKER: Nee sorry, gewoon betalen!", "MCDEWERKER: Nope! Absoluut niet! Betalen! En achteraan sluiten, ik zag u de rij skippen!"],
  "Hoe gaat het?": ["MCDEWERKER: Het gaat goed, bedankt!", "MCDEWERKER: Het gaat prima, met jou?", "MCDEWERKER: Goed hoor"],
  "*Skipt de rij*": ["MCDEWERKER: Dat zag ik!", "MCDEWERKER: NU ACHTERAAN SLUITEN!", "MCDEWERKER: U moet even in de rij gaan staan, iedereen wacht al erg lang, dus u moet dat ook!"],
  "Het gaat goed": ["MCDWERKER: Fijn om te horen!", "MCDEWERKER: Gelukkig maar, een goed humeur voor een heerlijke portie McDonald's!", "MCDEWERKER: Wat goed, dan zal je wel een nog grotere glimlach krijgen van een hapje McDonald's!"],
  "Het gaat slecht": ["MCDEWERKER: Wat vervelend, kan ik je opvrolijken met een paar gratis extraatjes?", "MCDEWERKER: Oh, nou geen zorgen, ons eten smaakt heerlijk, binnen no time staat er weer een mooie lach op je gezicht geplakt."],
  "Wat is er?": ["MCDEWERKER: Er is niks", "MCDEWERKER: Het is niks ergs", "MCDEWERKER: Niks eigenlijk"],
  "Waarom duurt het zo lang?": ["MCDEWERKER: Bent u zo ongeduldig? Even rustig aan hoor!", "MCDEWERKER: Omdat u heel veel besteld hebt en wij ook andere klanten moeten bedienen.", "Omdat u ongeduldig bent en wij dit moeten maken en dat tering veel moeite kost."],
  "Ik heb een vraag": ["MCDEWERKER: Ik ben benieuwd, wat is je vraag?", "MCDEWERKER: Wat is je vraag?", "MCDEWERKER: Vertel, ik zal het zo goed mogelijk proberen te beantwoorden"],
  "Waarom duurt het zo lang voordat ik mijn ijsje krijg?": ["MCDEWERKER: De ijsmachine wordt nu gerepareerd, hij is al een volledige eeuw of langer kapot geweest", "MCDEWERKER: Dat kan u niet besteld hebben, de machine is al 99.99999999999 jaar stuk", "Wees geduldig beste klant, we doen ons best, u hoeft nog maar drieduizend jaar te wachten, dan is de ijsmachine weer gerepareerd."],
  "Ik ben zo boos! Jullie moeten sluiten! Nu meteen!": ["MCDEWERKER: Oh nee he, niet weer zo'n karen...", "MCDEWERKER: Wat is er mis?", "MCDEWERKER: Vertel eens, waarom uit u ineens zo'n haat naar ons?"],
  "Mijn kind had hier kipnuggets vandaan gehaald en toen m'n lieve kindje die gisteren at werd het arme kind ziek! Hier is het bonnetje voor bewijs!": ["MCDEWERKER: Daar kunnen wij echt niets aan doen, kijk goed, die kipnuggets zijn van vijf jaar geleden.", "MCDEWERKER: Oke, dit kan me niks schelen, veel plezier met een ziek kind en verbannen zijn uit de McDonald's.", "MCDEWERKER: Nou hier zijn wat medicijnen, hopelijk wordt uw kind beter."],
  "Ik heb een klacht!": ["MCDEWERKER: Wat is uw klacht?", "MCDEWERKER: Nee, u hebt geen klacht maar u hebt wel toestemming om uit te glijden en in de modder te vallen."],
  "Ik haat jullie!": ["MCDEWERKER: Dat kan ons niks schelen, u bent toch lelijk.", "MCDEWERKER: BOEIE! Als u niet meer komt hoeven wij uw oorverdovende piepstem niet meer te horen, u lijkt wel een krijsende baby"],
  "Doe eens even normaal": ["MCDEWERKER: Het spijt me, ik moet inderdaad even normaal doen.", "MCDEWERKER: Oke, ik ga normaal doen.", "MCDEWERKER: Prima, ik doe normaal!!!!!"],
  "Wat zit er in de happy meal?": [ mcdonalds_happymeal_jewerly()],
  "Waarom mag ik geen ijsje bestellen?": ["MCDEWERKER: Omdat de ijsmachine kapot is, ga maar weg, de McDonald's sluit nu tijdelijk omdat alle Mcdewerkers naar de begrafenis gaan van onze geliefde en gewaardeerde ijsmachine, ondanks dat we hem nooit wilden helpen beter te worden.", "MCDEWERKER: Uhh onze ijsmachine wordt momenteel een beetje verwaarloosd, hij wordt mishandeld en kapot gemaakt.", "MCDEWERKER: Wij geven niks om onze ijsmachine en hebben hem mishandeld tot hij kapot ging.", "MCDEWERKER: Arme ijsmachine, hij is al sinds de oertijd kapot en wordt nooit meer gerepareerd want daar hebben wij geen budget voor en we gaan het niet zelf doen."],
  "Sinds wanneer is de ijsmachine kapot?": ["MCDEWERKER: Nog voor de Big Bang was onze ijsmachine aan het zweven en kromp in elkaar, wij wilden hem genezen maar het was te laat, door de Big Bang ontplofte hij en wij overleefden het.", "MCDEWERKER: Sinds hij gemaakt was, hij is een beetje misvormd.", "MCDEWERKER: Nou beste klant, nog voordat er ook maar iets bestond! Nog voordat er ook maar iets als de big bang kon komen, toen ging onze ijsmachine kapot."],
}

def get_answer(question): 
  if question in answers: 
      time.sleep(random.randint(1, 3))
      return answers[question] 
  else: 
      time.sleep(random.randint(1, 3))
      return "IK hoor je, je zei: " + question 

def process_answer(message):  
  time.sleep(random.randint(1, 3))
  for pattern in patterns: 
      match = re.search(pattern,message) 
      if match: 
          return patterns[pattern].format(match.group(1))
  
  if message in answers: 
      return random.choice(answers[message])
  else: 
      return "MCDEWERKER: Ik hoor je, je zei: " + message 
      
while True:
  message = input("YOU: ")
  answer = process_answer(message)
  print("Bot: " + answer)