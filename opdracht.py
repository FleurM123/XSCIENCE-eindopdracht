import re 
import time
import random

# Dictionary voor patronen.
patronen = { 
   "Do you remember (.*)":"Of course I remember {}", 
   "I feel (.*)":"Why do you feel {}?" 

# Dictionary voor veelvoorkomende berichten.

antwoorden = {
  "Hallo": ["MCDEWERKER: Hallo, hoe gaat het met jou?", "MCDEWERKER: Hoi!, hoe gaat het?", "MCDEWERKER: Hallo!"],
  "Hoe gaat het?": ["MCDEWERKER: Het gaat goed, bedankt!", "MCDEWERKER: Het gaat prima, met jou?", "MCDEWERKER: Goed hoor"],
  "Goed": ["MCDWERKER: Fijn om te horen!", "MCDEWERKER: Gelukkig maar, een goed humeur voor een heerlijke portie MCDonald's!", "MCDEWERKER: Fijn dat het goed met je gaat!"],
  "Wat is er?": ["MCDEWERKER: Er is niks", "MCDEWERKER: Jawel maar het is niks ergs", "MCDEWERKER: Niks eigenlijk"],
  "Ik heb een vraag": ["MCDEWERKER: Ik ben benieuwd, wat is je vraag?", "MCDEWERKER: Wat is je vraag?", "MCDEWERKER: Vertel, ik zal het zo goed mogelijk proberen te beantwoorden"],
  "Waarom duurt het zo lang voordat ik mijn ijsje krijg?": ["MCDEWERKER: De ijsmachine wordt nu gerepareerd, hij is een eeuw kapot geweest", "MCDEWERKER: Dat kan u niet bestelt hebben, de machine is stuk", "Wees geduldig beste klant, we doen ons best, u hoeft nog maar drieduizend jaar te wachten, dan is de ijsmachine weer gerepareerd."]
  
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


def krijg_antwoord_patroon(message):
  # Zoek een antwoord in de 'patterns' dictionary
  # en return dit antwoord als het is gevonden.
  for patroon in patronen: 
     match = re.search(patroon,message) 
     if match:
       # hint: patterns[pattern].xxx( ... ) waar xxx een python-functie is.
       # hint: lees hoofdstuk 4.2
       return "Hier komt het antwoord van de chatbot uit de patterns dictionary" 
  time.sleep(random.randint(1, 3))
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
      return "I don't understand you."

while True:
  bericht = input("YOU: ")
  antwoord = krijg_antwoord(bericht)
  print("Bot: " + antwoord)