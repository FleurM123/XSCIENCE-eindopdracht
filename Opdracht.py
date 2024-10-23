import re 

# Dictionary voor patronen.
patterns = { 
   "Do you remember (.*)":"Of course I remember {}", 
   "I feel (.*)":"Why do you feel {}?" 
}

# Dictionary voor veelvoorkomende berichten.
responses = {
  "Hallo": ["Hoi, hoe gaat you?", "Hello!"],
  "Het gaat best wel goed!": ["Da's fijn om te horen!", "Top!"]

}

# Functie die het antwoord van de chatbot teruggeeft.
def get_response(vraag): 
  if vraag in responses: 
      return responses[vraag] 
  else: 
      return "IK hoor je, je zei: " + vraag 

# Dit antwoord komt uit de patterns dictionary,
# de responses dictionary,
# of het is een standaardantwoord.


def get_response(message):
  # Zoek een antwoord in de 'patterns' dictionary
  # en return dit antwoord als het is gevonden.
  for pattern in patterns: 
     match = re.search(pattern,message) 
     if match:
        break
  if match       
  print("BOT: " + "So you feel, " + match.group(1)) 
  # hint: patterns[pattern].xxx( ... ) waar xxx een python-functie is.
       # hint: lees hoofdstuk 4.2
      #  return "Hier komt het antwoord van de chatbot uit de patterns dictionary" 
  
  # Zoek een antwoord in de 'responses' dictionary
  def get_response(vraag): 
    time.sleep(random.randint(1, 3))
    if vraag in responses: 
        return random.choice(responses[vraag])
    else: 
        return "CHATBOT: IK hoor je, je zei: " + vraag 
        
  # en return dit antwoord als het is gevonden.
  # Als het niet is gevonden, dan zegt de bot jou na.
  
    if message in responses:
        # hint: lees hoofdstuk 2.2 en hoofdstuk 3.3
        return "Hier komt het antwoord van de chatbot uit de responses dictionary"
    else:
        return "I don't understand you."

while True:
  message = input("YOU: ")
  response = get_response(message)
  print("Bot: " + response)



#   message = input()
# for pattern in patterns: 
#   match = re.search(pattern,message) 
#   if match:
#     break
# if match: 
#   print("BOT: " + "So you feel, " + match.group(1)) 
 
# else: 
#   print("BOT: "+ "I heard you but did not totally understand you, you said: " + message  )

