import json
from textwrap import indent

data = open("highscores.json" , 'a')

x = {
    "voornaam" : "bram",
    "achternaam" : "lenting",
    "leeftijd" : "18",
    "postcode" : "3318 AG"
    

}


y = json.dumps(x,indent=4)


data.write(y)


