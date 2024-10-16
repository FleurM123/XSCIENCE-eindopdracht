import re 
import time
import random

# Dictionary voor patronen.
patronen = { 
   "ik heb een vraag over (.*)":"MCDEWERKER: Oke!, je hebt een vraag over {}", 
   "Ik vind de McDonalds(.*)":"MCDEWERKER: Dus je vind de McDonalds {}?",
   "Ik heb een klacht over(.*)":"MCDEWERKER: Je hebt dus een klacht over {}?,
   "Ik vind het eten(.*)":"MCDEWERKER: Dus je vind het eten {}?",
   "Het ruikt hier naar (.*)":"MCDEWERKER: Ja? Ik ruik niet echt de geur van {}",
   "Jullie maken alles te (.*)":"MCDEWERKER: Oh echt? Dat is dan alleen uw mening, ik vind het niet zo {}"
   "Ik weet niet of ik hier nog eens kom, mijn ervaring was redelijk (.*)"


# Dictionary voor veelvoorkomende berichten.

antwoorden = {
  "Hallo": ["MCDEWERKER: Hallo, waarvoor komt u?", "MCDEWERKER: Hoi!, hoe gaat het?", "MCDEWERKER: Hallo, hoe kan ik je helpen?"],
  "Hoe gaat het?": ["MCDEWERKER: Het gaat goed, bedankt!", "MCDEWERKER: Het gaat prima, met jou?", "MCDEWERKER: Goed hoor"],
  "Het gaat goed": ["MCDWERKER: Fijn om te horen!", "MCDEWERKER: Gelukkig maar, een goed humeur voor een heerlijke portie McDonald's!", "MCDEWERKER: Wat goed, dan zal je wel een nog grotere glimlach krijgen van een hapje McDonald's!"],
  "Het gaat slecht": ["MCDEWERKER: Wat vervelend, kan ik je opvrolijken met een paar gratis extraatjes?", "MCDEWERKER: Oh, nou geen zorgen, ons eten smaakt heerlijk, binnen no time staat er weer een mooie lach op je gezicht geplakt."],
  "Wat is er?": ["MCDEWERKER: Er is niks", "MCDEWERKER: Jawel maar het is niks ergs", "MCDEWERKER: Niks eigenlijk"],
  "Ik heb een vraag": ["MCDEWERKER: Ik ben benieuwd, wat is je vraag?", "MCDEWERKER: Wat is je vraag?", "MCDEWERKER: Vertel, ik zal het zo goed mogelijk proberen te beantwoorden"],
  "Waarom duurt het zo lang voordat ik mijn ijsje krijg?": ["MCDEWERKER: De ijsmachine wordt nu gerepareerd, hij is een eeuw kapot geweest", "MCDEWERKER: Dat kan u niet bestelt hebben, de machine is stuk", "Wees geduldig beste klant, we doen ons best, u hoeft nog maar drieduizend jaar te wachten, dan is de ijsmachine weer gerepareerd."],
  "Ik ben zo boos! Jullie moeten sluiten! Nu meteen!": ["MCDEWERKER: Oh nee he, niet weer zo'n karen...", "MCDEWERKER: Wat is er mis?", "MCDEWERKER: Vertel eens, waarom uit u ineens zo'n haat naar ons?"],
  "Mijn kind had hier kipnuggets vandaan gehaald en toen m'n lieve kindje die gisteren at werd het arme kind ziek! Hier is het bonnetje voor bewijs!": ["MCDEWERKER: Daar kunnen wij echt niets aan doen, kijk goed, die kipnuggets zijn van vijf jaar geleden.", "MCDEWERKER: Oke, dit kan me niks schelen, veel plezier met een ziek kind en verbannen zijn uit de McDonald's.", "MCDEWERKER: Nou hier zijn wat medicijnen, hopelijk wordt uw kind beter."],
  "Ik heb een klacht!": ["MCDEWERKER: Wat is uw klacht?"]
  
}


def krijg_antwoord(vraag): 
  if vraag in antwoorden: 
      time.sleep(random.randint(1, 3))
      return antwoorden[vraag] 
  else: 
      time.sleep(random.randint(1, 3))
      return "IK hoor je, je zei: " + vraag 

# Dit antwoord komt uit de patterns dictionary,
# de responses dictionary,
# of het is een standaardantwoord.


def krijg_antwoord_patroon(bericht):
    # Zoek een antwoord in de 'patterns' dictionary
    # en return dit antwoord als het is gevonden. 
    time.sleep(random.randint(1, 3))
    for patroon in patronen: 
        match = re.search(patroon,bericht) 
        if match: 
            return patterns[pattern].format(match.group(1))
    
    if vraag in antwoorden: 
        return random.choice(antwoorden[vraag])
    else: 
        return "MCDEWERKER: IK hoor je, je zei: " + vraag 
  

  
      
  # en return dit antwoord als het is gevonden.
  # Als het niet is gevonden, dan zegt de bot jou na.

  if bericht in antwoorden:
      # hint: lees hoofdstuk 2.2 en hoofdstuk 3.3
      return "Hier komt het antwoord van de chatbot uit de responses dictionary"
  else:
      return "Ik begrijp je niet, kan je je vraag opnieuw stellen?"

while True:
  bericht = input("YOU: ")
  antwoord = krijg_antwoord(bericht)
  print("Bot: " + antwoord)